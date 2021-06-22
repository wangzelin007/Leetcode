# 描述
# 给定一个字符串描述的算术表达式，计算出结果值。
# 输入字符串长度不超过100，合法的字符包括”+, -, *, /, (, )”，”0-9”，
# 字符串内容的合法性及表达式语法的合法性由做题者检查。本题目只涉及整型计算。
s=input()
s=s+(")")#输入
st=[]#放入数字
so=[]#放入操作
so.append("(")

#st为存数字的栈，在这段代码里会处理好数字计算和更新两个栈,so会保留左括号
def cal_data(st,so):
    num=0#结果的数字
    num1=st[-1]#栈顶，分母的位置，可能出现为0的错误
    st.pop()
    num2=st[-1]
    st.pop()
    op=so[-1]
    so.pop()
    if(op=="+"):
        num=num1+num2
    elif(op=="-"):
        num=num2-num1
    elif(op=="*"):
        num=num2*num1
    elif(op=="/"):
        num=num2/num1
    st.append(num)
    return

##当前运算符与符号栈的栈顶运算符做优先级比较，如果当前优先级高，则不做运算压入栈中;相同或者低都可以进行计算
def compare_op(op1,so):#op1为输入字符串中，当前的元素。op2为符号栈的栈顶元素
    op2=so[-1]
    if (op2=="(" or op2=="[" or op2=="{" ):
        return False
    elif (op2=="+" or op2=="-") and (op1=="*" or op1=="/"):
        return False
    else:
        return True

string_mp =[ "+" , "-" , "*" , "/" , ")" , "]" , "}" ]
nextIsOp=False
i=0
while i <len(s):#不包括第len(s)个
    if (s[i]=="(" or s[i]=="{" or s[i]=="["):
        so.append(s[i])
        i=i+1
    elif (s[i]==")" or s[i]=="]" or s[i]=="}"):
        while(so[-1]!="(" and so[-1]!="[" and so[-1]!="{"):
            if(compare_op(s[i],so)):
                cal_data(st,so)
        so.pop()
        i=i+1
    elif(nextIsOp):
        while(compare_op(s[i],so)):
            cal_data(st,so)
        so.append(s[i])
        nextIsOp=False#此处又要回到开始状态
        i=i+1
    else:
        j=i
        if s[j]=="-":
            i=i+1
        while(s[i] not in string_mp):
            i=i+1
        num=s[j:i]
        st.append(int(num))
        nextIsOp=True
print (st[0])
