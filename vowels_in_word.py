#Vowel Count

counter=0
counter1=0
vowelCount=0
numStr = input("Enter number of sentences: ")

numInt = int(numStr)
numWord = []
numLetter = []
for counter in range(0,numInt):
    numWord.append(input('Enter the word:'))
print ('You Entered - ', numWord)

for counter in range(0,numInt):
    wordlen=len(numWord[counter])
    for counter1 in range(0,wordlen):
        alphabet = numWord[counter]
        #print(counter,":",counter1,":",'Word-->',numWord[counter],":",'Individual Letter-->',alphabet[counter1:counter1+1])

        if ((alphabet[counter1:counter1+1] == "a") or (alphabet[counter1:counter1+1] == "e") or (alphabet[counter1:counter1+1] == "i") or (alphabet[counter1:counter1+1] == "o") or (alphabet[counter1:counter1+1] == "u")):
            vowelCount = vowelCount + 1

    print("Sentence[",counter+1,"]:",numWord[counter], ":Vowel Count->", vowelCount)                    
    vowelCount=0
