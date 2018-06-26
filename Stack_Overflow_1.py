WordList = []
letterSearchList=[]
count=0

wordInput = input("Please Enter A Word: ")
letterSearch = input("Input your search letter: ")
WordList.append(wordInput.lower())

for word in WordList:
    letterSearchList = list(word) # This will create a list of the item in WordList
    for item in letterSearchList:
        if (item==letterSearch):
            count = count + 1
print(letterSearch, ' appeared ',count,' times in the word - ',wordInput)
    
