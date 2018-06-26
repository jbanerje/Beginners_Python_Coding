#Weighted Sum

counter=0;
sumRemainder=0;

userInput = int(input("Enter a num: "))

while (userInput > 10):
    counter = counter + 1

    inputQuotient = int (userInput / 10)
    inputRemainder = userInput % 10

    sumRemainder = sumRemainder + (inputRemainder * counter)
    userInput = inputQuotient
    #print (inputQuotient,inputRemainder,sumRemainder )

counter=counter + 1
sumRemainder = sumRemainder + userInput * counter
#print (inputQuotient,inputRemainder,sumRemainder )
print ("Weighted Sum: ", sumRemainder)

