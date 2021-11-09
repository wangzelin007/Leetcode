details = None

err=[]
for detail in details or []:
    err.append(detail)
print(err)

something = None
empty = something or {}
print(empty)  # {}

# TypeError: 'NoneType' object is not iterable
# err=[]
# for detail in details:
#     err.append(detail)
# print(err)
