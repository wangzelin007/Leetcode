# NF表示目前的记录被分割的字段的数目，NF可以理解为Number of Field。
# NR可以理解为Number of Row。
# FNR可以理解为每个文件的 Number of Row

awk '{print FILENAME,"NR="NR,"FNR="FNR,"$"NF"="$NF}' file1.txt file2.txt
# $0 表示所有列
# file1.txt NR=1 FNR=1 $3=87
# file1.txt NR=2 FNR=2 $3=88
# file1.txt NR=3 FNR=3 $3=86
# file2.txt NR=4 FNR=1 $4=90
# file2.txt NR=5 FNR=2 $4=92
awk '{print FILENAME,"NR="NR,"FNR="FNR,"data="$0}' file1.txt file2.txt