import sys

from covgen.run.inputgenerator import InputGenerator


def print_help():
    print('Usage: python inputgenerator.py <target file location>')
    print(
        '       python inputgenerator.py <target file location> --function <target function name> --method <method name=avm or hillclimbing> --retry-count <retry_count> --int-min <minimum int> --int-max <maximum int>')
    print(
        '       python inputgenerator.py <target file location> -f <target function name> -m <method name=avm or hillclimbing> -r <retry_count>')


def execute():
    if len(sys.argv) < 2:
        print_help()
        exit(1)

    target_file = sys.argv[1]
    target_function = None
    search_method = None
    retry_count = 100
    int_min = -10000
    int_max = 10000

    index = 2
    while index + 1 < len(sys.argv):
        option = sys.argv[index]
        if option == '-f' or option == '--function':
            target_function = sys.argv[index + 1]

        elif option == '-m' or option == '--method':
            search_method = sys.argv[index + 1]

        elif option == '-r' or option == '--retry-count':
            retry_count = int(sys.argv[index + 1])

        elif option == '--int-min':
            int_min = int(sys.argv[index + 1])

        elif option == '--int-max':
            int_max = int(sys.argv[index + 1])

        else:
            print('unknown option: {}'.format(option))
            print_help()
            exit(1)

        index = index + 2

    generator = InputGenerator(
        target_file,
        target_function,
        method=search_method,
        retry=retry_count
    )

    generator.generate_all_inputs_and_print()


if __name__ == "__main__":
    execute()
