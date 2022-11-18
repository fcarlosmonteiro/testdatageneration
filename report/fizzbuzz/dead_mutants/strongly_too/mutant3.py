import sys


"""
FIZZBUZZ

Description: FizzBuzz is a typical coding interview question. Numbers 1 - x are printed;
if they are divisible by 3, the number is replaced with `Fizz`, if the number is divisible by 5,
the number is replaced with `Buzz`, if the number is divisible by 15,
the number is replaced with `FizzBuzz`.

Usage: iterations=50 venv/bin/python FizzBuzz.py

Lessons Learned:
1) Order matters, ensure that FizzBuzz is first or it could have criteria met for just
Fizz or Buzz
"""


def generate_fizzbuzz(iterations):
    """Iterate through numbers and print FizzBuzz to console."""
    iterations = int(float(iterations))
    output = ''
    if _validate_iterations(iterations):
        return 'iterations must be greater than or equal to 1.'

    for iteration in range(1, iterations + 1):
        output += _determine_output(iteration) + ' '
    return output


def _validate_iterations(iterations):
    """Validate the iterations before proceeding."""
    return iterations < 1


def _determine_output(iteration) -> str:
    """Determine what the output of each iteration is based on its divisibility."""
    fizz = iteration % 3 == 0
    buzz = iteration % 5 == 0

    if fizz and buzz:
        output = 'FizzBuzz'
    elif not fizz: #PM | type_kill=weakly args=[-8948.25] | type_kill=strongly args=[4699.99]
        output = 'Fizz'
    elif buzz:
        output = 'Buzz'
    else:
        output = str(iteration)

    return output


if __name__ == '__main__':
    iterations = sys.argv[1:][0]
    print(generate_fizzbuzz(iterations))