import ast
string = "['xxx','yyy','zzz']"
output = ast.literal_eval(string)
print(output)
# output = ['xxx', 'yyy', 'zzz']

output=eval(string)
print(output)
# output = ['xxx', 'yyy', 'zzz']

output=list(string)
print(output)
# output = ['[', "'", 'x', 'x', 'x', "'", ',', "'", 'y', 'y', 'y', "'", ',', "'", 'z', 'z', 'z', "'", ']']