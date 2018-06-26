# ----------------------------------------------------------------------
# Title             : Class Example
# Author            : Jagannath Banerjee
# Date              : 12/15/2017
# ----------------------------------------------------------------------

#Import Library Block
import os

#class definition
class library(object):

    #initializing
    def __init__(self,name,author,date,issue=False):
        self.name = name
        self.author = author
        self.date = date
        self.issue = issue
        
    #getter
    def getName(self):
        return self.name

    def getAuthor(self):
        return self.author

    def getAuthor(self):
        return self.date     

    def getAuthor(self):
        return self.issue
    
    #setter
    def upateDate(self,setUpdateDate):
        self.date = setUpdateDate
    
    #Txt string class
    def __str__(self):
        return "Person[Book name= " + self.name + " from " + self.author + " Issued sucessfully!] "

#Main Function
def main():

    lib = library('Book1','Jagannath','12/15/2017',True)
    print(lib.getName())
    print(lib)
    
           
#Main Function Call
if __name__=="__main__":
    main()
