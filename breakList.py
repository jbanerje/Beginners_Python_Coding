# Breaking the user entered list into multiple lists.
shopList = []
shopListA = [] 
shopListB = []
counter = 0

#taking user entered list
maxLengthList = int(input('How many items: '))

while len(shopList) < maxLengthList:
    item = input("Enter your Item to the List: ")
    shopList.append(item)
print ("That's your Shopping List",shopList)


#breaking the list
breakLengthList = int(input('How many items want to break in first list: '))

while (counter < breakLengthList):
        shopListA.append(shopList[counter])
        counter = counter + 1
print ("List A : ", shopListA)

while (counter < len(shopList)):
       shopListB.append(shopList[counter])
       counter = counter + 1
print ("List B : ", shopListB)
