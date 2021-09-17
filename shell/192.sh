# Write a bash script to calculate the frequency of each word in a text file words.txt.
# For simplicity sake, you may assume:
# words.txt contains only lowercase characters and space ' ' characters.
# Each word must consist of lowercase characters only.
# Words are separated by one or more whitespace characters.
# Example:
# Assume that words.txt has the following content:
# the day is sunny the the
# the sunny is is
# Your script should output the following, sorted by descending frequency:
# the 4
# is 3
# sunny 2
# day 1
# Note:
# Don't worry about handling ties, it is guaranteed that each word's frequency count is unique.
# Could you write it in one-line using Unix pipes?
# 按第一列排序了不对 sort -rnk 2
awk '{for(i=1;i<=NF;i++){asso_array[$i]++;}};END{for(w in asso_array){print w,asso_array[w];}}' 192.txt | sort -rn

cat 192.txt |
awk '{
    for(i=1;i<=NF;i++){
        count[$i]++
    }
} END {
    for(k in count){
        print k" "count[k]
    }
}' |
sort -rnk 2

# cat 192.txt | xargs -n1 | sort | uniq -c | sort -rn
# 4 the
# 3 is
# 2 sunny
# 1 day
cat 192.txt | xargs -n1 | sort | uniq -c | sort -rn | awk '{print $2,$1}'
