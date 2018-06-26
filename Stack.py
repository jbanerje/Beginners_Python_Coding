#Dec 2 Binary conversion

binary_num=[]

decimal_num = int(input("Enter a decimal number :"))

while decimal_num > 1 :
    binary_num.append(decimal_num % 2)
    decimal_num = ( decimal_num // 2 )

binary_num.append(decimal_num)
print("binary_num:", binary_num)

binary_num.reverse()

print("binary_num:", binary_num)
