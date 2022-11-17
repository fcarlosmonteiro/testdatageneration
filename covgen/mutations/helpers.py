import os
import shutil


def handle_mutant_with_logic_error(filename):
  cwd = os.getcwd()
  shutil.move('{}/{}'.format(cwd, filename), '{}/.tmp/mutants_with_logic_error/'.format(cwd))