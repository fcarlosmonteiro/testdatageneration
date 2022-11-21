import os, random, shutil

from covgen.mutations.helpers import handle_add_of_value_that_killed_mutant


class RandomTest():
    def __init__(self, path_original, amount_mutants, amount_of_data_set, amount_of_data_paths, int_min, int_max):
        self.path_original = path_original
        self.amount_mutants = amount_mutants
        self.amount_of_data_set = amount_of_data_set
        self.amount_of_data_paths = amount_of_data_paths
        self.int_min = int_min
        self.int_max = int_max    


    def execute(self):
        cwd = os.getcwd()
        matrix_args = []
        path_name, type_format = self.path_original.split('.')
        path, filename = path_name.split('/')

        path_mutants = '{}/random_test/mutants/{}'.format(cwd, filename)
        for i in range(self.amount_of_data_set):
            new_args = []
            for j in range(self.amount_of_data_paths):
                new_agr = random.uniform(self.int_min, self.int_max)
                new_args.append(new_agr)
            matrix_args.append(new_args)
        
        list_mutants = []
        for nmut in range(self.amount_mutants):
            list_mutants.append(nmut+1)
        
        print("[{}]".format(filename))
        for args in matrix_args:
            args_str = ' '.join(map(str, args))
            script = 'python {}/{} {}'.format(cwd, self.path_original, args_str) 
            stream = os.popen(script)
            result_original = str(stream.read())
            print("Random Inputs -> {}".format(args_str))
            for nmut in list_mutants:
                try:
                    script = 'python {}/mutant{}.py {}'.format(path_mutants,nmut, args_str)
                    stream = os.popen(script)
                    result_mutant = str(stream.read())
                    if result_original != result_mutant:
                        handle_add_of_value_that_killed_mutant('random_test/mutants/{}/mutant{}.py'.format(filename, nmut), args, 'random')
                        shutil.move('{}/mutant{}.py'.format(path_mutants, nmut), '{}/dead_mutants'.format(path_mutants))
                        list_mutants.remove(nmut)
                except:
                    print("Error no mutante {}".format(nmut))
                    continue
        
