import os
import shutil


class Mutation:
    def __init__(self, file):
        target = file
        path_name, type_format = file.split('.')
        unit_test = '{}_test.{}'.format(path_name, type_format)
        self._mutants_generator(target, unit_test)

    def _mutants_generator(self, target, unit_test):
        stream = os.popen('mut.py --target {} --unit-test {} -m'.format(target, unit_test))
        output = stream.read()
        mutants_op = output.split('--------------------------------------------------------------------------------')

        count = 0
        op_mut = []
        for mutant in mutants_op:
            if count % 2 != 0:
                op_mut.append(mutant)
            count += 1

        num = 1
        cwd = os.getcwd()

        path = '{}/.tmp'.format(cwd)

        try:
            shutil.rmtree(path)
        except OSError as error:
            pass

        os.mkdir(path)

        for m in op_mut:
            m = m.split('\n')
            count = 0
            for x in m:
                if x[:1] == '-':
                    path_mutant = '{}/.tmp/mutant{}.py'.format(cwd, str(num))
                    file_mutant = open(path_mutant, 'w')
                    prog_original = open('{}/{}'.format(cwd, target))
                    for line in prog_original:
                        if line.replace('\n', '') == x[6:]:
                            file_mutant.write(m[count + 1][6:] + ' #PM\n')
                            num += 1
                            continue
                        file_mutant.write(line)
                    file_mutant.close()
                    prog_original.close()
                count += 1

        print(num)
