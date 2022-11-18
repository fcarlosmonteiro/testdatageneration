import os
import shutil


def handle_mutant_with_logic_error(filename):
  cwd = os.getcwd()
  shutil.move('{}/{}'.format(cwd, filename), '{}/.tmp/mutants_with_logic_error/'.format(cwd))

def handle_add_of_value_that_killed_mutant(filename, args, type_kill):
  cwd = os.getcwd()
  path_mutant = '{}/{}'.format(cwd, filename)
  old_file_mutant = open(path_mutant)
  file_mutant = open('{}.txt'.format(path_mutant) , "w")

  for line in old_file_mutant:
    if '#PM' in line:
      line = line.replace('\n', '')
      line += ' | type_kill={} args={}\n'.format(type_kill, str(args))
    file_mutant.write(line)
  file_mutant.close()
  old_file_mutant.close()
  shutil.move('{}.txt'.format(path_mutant), path_mutant)