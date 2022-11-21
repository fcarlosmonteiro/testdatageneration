import sys

from random_test.run.random_test import RandomTest


def execute():
    path_original = ''
    amount_mutants = 1
    amount_of_data_set = 1
    amount_of_data_paths = 1
    int_min = -10000
    int_max = 10000

    index = 1
    while index + 1 < len(sys.argv):
        option = sys.argv[index]

        if option == '--path-original':
            path_original = sys.argv[index + 1]

        elif option == '--amount-mutants':
            amount_mutants = int(sys.argv[index + 1])
        
        elif option == '--amount-of-data-set':
            amount_of_data_set = int(sys.argv[index + 1])

        elif option == '--amount-of-data-paths':
            amount_of_data_paths = int(sys.argv[index + 1])

        elif option == '--int-min':
            int_min = int(sys.argv[index + 1])

        elif option == '--int-max':
            int_max = int(sys.argv[index + 1])

        index = index + 2

    random_test = RandomTest(
        path_original,
        amount_mutants,
        amount_of_data_set,
        amount_of_data_paths,
        int_min,
        int_max
    )

    random_test.execute()



if __name__ == "__main__":
    execute()
