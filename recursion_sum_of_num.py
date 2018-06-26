#Recursion - sum of numbers

def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]
        print ("In 1 :" , numlist[0])
    else:
        print ("In 2 :" , numlist[0])
        print ("in 2 :", numlist[1:])
        return numlist[0] + listsum(numlist[1:])
    

def main():
    # my code here
    #print("Hello World")
    print(listsum([1,3,5,7,9]))

if __name__ == "__main__":
    main()
