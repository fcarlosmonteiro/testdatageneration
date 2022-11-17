import copy, os, shutil

import covgen.types.branchutil as branchutil
import covgen.mutations.generation as generation_mutations


from covgen.mutations.helpers import handle_mutant_with_logic_error

from covgen.exceptions.no_target_function_exception import NoTargetFunctionException

from covgen.parser.ast_parser import ASTParser

from covgen.localsearch.fitnesscalc import FitnessCalculator
from covgen.localsearch.hillclimbing import HillClimbing
from covgen.localsearch.avm import AVM


class InputGenerator():
    def __init__(self, file, function_name=None, method=None, retry=100, generate_mutants=False, int_min=0,
                 int_max=3000):
        parser = ASTParser(file)

        self.method = method
        self.filename = file
        self.retry_count = retry
        self.function_defs = parser.function_defs
        self.AST = parser.AST
        self.target_function = None

        self.int_min = int_min
        self.int_max = int_max

        if generate_mutants:
            amount_of_mutants = generation_mutations.generate(file)

            self.mutants = []
            self.dead_mutants = []

            for mut in range(amount_of_mutants):
                filename = '.tmp/mutant{}.py'.format(str(mut + 1))
                try:
                    mutant = InputGenerator(filename, function_name, method, retry)
                    self.mutants.append(mutant)
                except:
                    handle_mutant_with_logic_error(filename)

        if function_name is not None:
            try:
                self._set_target_function(function_name)

            except NoTargetFunctionException as err:
                print('{}: {}'.format(err.message, err.name))
                exit(1)

    def _set_target_function(self, name):
        for f in self.function_defs:
            if f.name == name:
                target_function = copy.deepcopy(f)

                target_function.insert_hooks_on_predicates()
                self.target_function = target_function
                return

        raise NoTargetFunctionException(
            name, 'Cannot find target function definition with given name')

    def _print_branch_tree(self):
        if self.target_function is not None:
            self.target_function.branch_tree.print()

    def _generate_input(self, target_branch_id, list_args=[]):
        if self.target_function is None:
            print('Please set target function!')
            return

        fitness_calculator = FitnessCalculator(
            self.target_function, target_branch_id, self.AST)

        mutants_fitness_calculator = []
        for mutant in self.mutants:
            mutants_fitness_calculator.append(FitnessCalculator(
                mutant.target_function, target_branch_id, mutant.AST))

        searcher = None
        if self.method == 'avm':
            searcher = AVM(fitness_calculator, self.retry_count)

        elif self.method == 'hillclimbing':
            searcher = HillClimbing(
                fitness_calculator,
                mutants_fitness_calculator,
                self.retry_count,
                int_min=self.int_min,
                int_max=self.int_max,
            )

        else:
            # mix possible methods
            searcher = AVM(fitness_calculator, self.retry_count)
            minimised_args, fitness_value = searcher.minimise()

            if fitness_value == 0:
                return minimised_args

            else:
                searcher = HillClimbing(fitness_calculator, self.retry_count)

        minimised_args, fitness_value = searcher.minimise(list_args)

        branch_type = branchutil.parse_branch_type(target_branch_id)
        cwd = os.getcwd()
        for mutant in self.mutants:
            mutant_fitness_calculator = FitnessCalculator(
                mutant.target_function, target_branch_id, mutant.AST)
            try:
                result_for_the_branch = mutant_fitness_calculator.calculate_mutante(minimised_args)
                if branch_type != result_for_the_branch:
                    self.dead_mutants.append(mutant)
                    self.mutants.remove(mutant)
                    shutil.move('{}/{}'.format(cwd, mutant.filename), '{}/.tmp/dead_mutants/'.format(cwd))
            except:
                self.mutants.remove(mutant)
                handle_mutant_with_logic_error(mutant.filename)

        if fitness_value == 0:
            return minimised_args

        else:
            return None

    def generate_all_inputs(self):
        next_target_functions = []
        mutant_next_target_functions = []
        all_inputs = {}

        for mutant in self.mutants:
            if mutant.target_function is None:
                for f in mutant.function_defs:
                    mutant_next_target_functions.append(f.name)

                mutant._set_target_function(mutant_next_target_functions.pop())

        if self.target_function is None:
            for f in self.function_defs:
                next_target_functions.append(f.name)

            self._set_target_function(next_target_functions.pop())

        mutant_branches = []

        for mutant in self.mutants:
            mutant_branch_tree = mutant.target_function.branch_tree
            mutant_branches.append(mutant_branch_tree.get_all_branches())

        while True:
            branch_tree = self.target_function.branch_tree

            branches = branch_tree.get_all_branches()

            inputs = {}

            list_args = []

            for branch in branches:
                branch_id = branchutil.create_branch_id(branch)


                args = self._generate_input(branch_id, list_args)
                list_args = args
                inputs[branch_id] = args

                parents = branch_tree.get_nodes_on_path(branch_id)[1:]

                for branch in parents:
                    parent_id = branchutil.create_branch_id(branch)

                    if inputs[parent_id] == None:
                        inputs[parent_id] = args

            all_inputs[self.target_function.name] = inputs

            if len(next_target_functions) == 0:
                break

            self._set_target_function(next_target_functions.pop())

        return all_inputs

    def generate_all_inputs_and_print(self):
        all_inputs = self.generate_all_inputs()

        for function_name, inputs in all_inputs.items():
            print('[{}]'.format(function_name))

            if len(inputs.items()) == 0:
                print('no branch detected')

            for branch_id, args in sorted(inputs.items(), key=branchutil.compare_branch_id):
                line = '{}: Inputs->'.format(branch_id)
                if args is None:
                    line += ' -'
                else:
                    for arg in args:
                        line += ' {}'.format(arg)

                print(line)

            print('')
            print(".......FIM.......")
