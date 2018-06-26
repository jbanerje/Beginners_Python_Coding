#Maximum of array -  Linear Search

sumTotal=0;
counter=0;
counter_min=0;
numList=[5,15,6,13,20,21,42,22,8]

# Search for the max number
print("=========searching max number================================")
for counter in range(len(numList)-1):
    if counter == 0 :
       firstNum=numList[counter]
    else:
       firstNum= maxNum
       
    nxtNum=numList[counter + 1]

    if (firstNum > nxtNum) :
        maxNum = firstNum
    else :
        maxNum = nxtNum
        
       
    print("Loop Logic - " ,firstNum,":",nxtNum,"Choose->", maxNum)
    
print("Max Number of array is  ->",maxNum)

# Search for the max number
print("=========searching min number================================")
for counter_min in range(len(numList)-1):
    if counter_min == 0 :
       firstNum=numList[counter_min]
    else:
       firstNum= maxNum
       
    nxtNum=numList[counter_min + 1]

    if (firstNum < nxtNum) :
        maxNum = firstNum
    else :
        maxNum = nxtNum
        
       
    print("Loop Logic - " ,firstNum,":",nxtNum,"Choose->", maxNum)
    
print("Mimimum Number of array is  ->",maxNum)
