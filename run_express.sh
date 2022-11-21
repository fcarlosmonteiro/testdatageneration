#!/bin/bash

while getopts p:q:a:r flag
do
    case "${flag}" in
        a) name=${OPTARG};;
        p) path=${OPTARG};;
        q) qtd=${OPTARG};;
        r) retry_count=${OPTARG};;
    esac
done


rm -rf run_express/$name
mkdir run_express/$name

for (( c=1; c<=$qtd; c++ ))
do
  mkdir run_express/$name/values$c/
  echo "------------values$c-----------------"

  python -m covgen $path -m hillclimbing -r $retry_count >> run_express/$name/values$c/input.txt
  mv .tmp/* run_express/$name/values$c/

  alive=$(ls run_express/$name/values$c/ -l|grep -e "py"|wc -l)
  logi_error=$(ls run_express/$name/values$c/mutants_with_logic_error/ -l|grep -e "py"|wc -l)
  ls run_express/$name/values$c/dead_mutants/ >> .tmp.txt
  ls run_express/$name/values$c/dead_mutants/strongly_too >> .tmp.txt
  kill_W=$(ls run_express/$name/values$c/dead_mutants/ -l|grep -e "py"|wc -l)
  kill_S=$(ls run_express/$name/values$c/dead_mutants/strongly_too/ -l|grep -e "py"|wc -l)

  echo "vivos: $alive" >> run_express/$name/values$c/input.txt
  weak=$(($kill_W + $logi_error))
  strong=$(($kill_S + $weak))
  total=$(($kill_W + $kill_S + $logi_error + $alive))
  echo "weak: $weak" >> run_express/$name/values$c/input.txt
  echo "strong: $strong" >> run_express/$name/values$c/input.txt
  echo "total: $total" >> run_express/$name/values$c/input.txt
  cat run_express/$name/values$c/input.txt
  rm .tmp.txt
  echo "------------------------------------"
done

