# Given a text file file.txt, transpose its content.
# You may assume that each row has the same number of columns, and each field is separated by the ' ' character.
#
# Example:
# If file.txt has the following content:
# name age
# alice 21
# ryan 30
# Output the following:
# name alice ryan
# age 21 30

awk '{for(i=1;i<=NF;i++){if(NR==1){row[i]=$i} else{row[i]=row[i]" "$i}}};END{for(i=1;i<=NF;i++){print row[i]}}' 194.txt

#!/bin/env bash

column=$(awk '{print NF}' 194.txt | uniq)
# echo $column
for ((i=1;i<=column;i++))
do
#   cut -d' ' -f$i 194.txt|xargs
  awk '{print $'''$i'''}' 194.txt | xargs
done

columns=$(cat 194.txt | head -n 1 | wc -w)
# echo $columns
for i in $(seq 1 $columns)
do
  awk '{print $'''$i'''}' 194.txt | xargs
done