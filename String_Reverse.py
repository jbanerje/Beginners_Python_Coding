#String Reverse

list1=[]
inp_str = input("enter a string:")

str_len = len(inp_str)

for i in range(str_len-1, -1, -1):

    print(inp_str[i])
    list1.append(inp_str[i])

print(list1)


    


    
