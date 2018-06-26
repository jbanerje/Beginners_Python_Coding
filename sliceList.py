# Extracting a slice from the list.
shopList = []
shopListA = [] 

counter = 0

#taking user entered list
maxLengthList = int(input('How many items: '))

while len(shopList) < maxLengthList:
    item = input("Enter your Item to the List: ")
    shopList.append(item)
print ("That's your Shopping List",shopList)


#Slicing the list
breakListStart = int(input('Enter the starting position: '))
breakListEnd = int(input('Enter the length: '))

while (breakListStart <= breakListEnd):
        shopListA.append(shopList[breakListStart])
        breakListStart = breakListStart + 1
print ("New List : ", shopListA)
