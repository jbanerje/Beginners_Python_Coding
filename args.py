#Args

def sum(*args):
    print(args)
    print(type(args))
    sum=0
    for arg in args:
        sum=sum+arg
    return(sum)

result=sum(2,3,46,7,8)
print("Result:",result)

