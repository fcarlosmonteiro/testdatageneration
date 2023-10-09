# Weak Mutation Test Data Generation

A Python implementation of automated test data generation.

Currently, it works only for the subset of Python functions satisfying these conditions:

- takes only integer arguments
- new: integer and float arguments

- had only integer type local variables

- contains predicates that only involve relational operators (==, !=, <, >, <=, >=), integer variables, and calls to functions with integer return type

## Run from Source

```bash
python -m covgen target/boolop.py -m hillclimbing
```
## This app was developed based on https://github.com/greenmonn/sbst-input-generator for structural testing
