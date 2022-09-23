print(72.9286 ** 0.5)
print(59.4886 ** 0.5)
# a = '{:.4f}'.format(1.0000)
# print(a)
# 8.539824354165606
# num1 = '{:.4f}'.format(8.5398)
# 7.712885322627324
# num1 = '{:.4f}'.format(7.7129)
# num0 = '{:.4f}'.format(72.9286)
# num1 = '{:.4f}'.format(7.7129)
# num1 = '{:.4f}'.format(72.9286)
# num0 = '{:.4f}'.format(72.9286)
# num1 = '{:.4f}'.format(59.4886)
# num0 = '{:.4f}'.format(59.4886)
# num2 = num0 / num1
# print(round(num2, 4))
# print(str(round(num2, 4))[5])

while True:
    print(num1)
    while len(str(num1)) in [6, 7] and str(num1)[-1] not in ['0', '5']:
        num1 = round(float(num1), 4)
        num1 -= 0.0001
        # num1 = round(num1, 4)
    print('num1')
    print(num1)
    num2 = '{:.4f}'.format(round(float(num0) / num1, 4))
    print(num2)
    if str(num2)[-1] in ['0', '5']:
        if round(float(num1) * float(num2), 4) == num0:
            print('found num2')
            print(num2)
            break
        else:
            num1 -= 0.0001
            # num1 = round(num1, 4)
    else:
        num1 -= 0.0001
        # num1 = round(num1, 4)



