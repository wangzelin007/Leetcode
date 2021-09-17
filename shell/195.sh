Given a text file file.txt, print just the 10th line of the file.
Example:
# Assume that file.txt has the following content:
# Line 1
# Line 2
# Line 3
# Line 4
# Line 5
# Line 6
# Line 7
# Line 8
# Line 9
# Line 10
# Your script should output the tenth line, which is:
# Line 10

row_num=$(cat 195.txt | wc -l)
echo $row_num
if [ $row_num -lt 10 ];then
    echo "The number of row is less than 10"
else
    awk '{if(NR==10){print $0}}' 195.txt
fi

# grep -n "" 195.txt | grep -w '10' | cut -d: -f2
# sed -n '10p' 195.txt
# awk '{if(NR==10){print $0}}' 195.txt