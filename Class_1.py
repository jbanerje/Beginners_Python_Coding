# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 12:08:30 2017
OOP-1
@author: jagan
"""
class Person(object):
    #Explanation - Creating a Person class
    
    #Constructor(Initialization)
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email
        
    #Getters(Accesors Method)
    def getName(self):
        return self.name
    
    def getPhone(self):
        return self.phone
    
    def getEmail(self):
        return self.email
    
    #Setters(Mutators Method)
    def setPhone(self,newPhoneNumber):
        self.phone = newPhoneNumber
    
    def setEmailAddress(self,newEmailAddress):
        self.email = newEmailAddress    
    
    #def String to print friend1. This is inherited from object class
    def __str__(self):
        return "Person[name=" + self.name + " Phone-" + str(self.phone) + " Email-" + self.email+"]"
        
#Main Function
def main():
    #print("Hello")
    friend1 = Person('Jagan',111,'a@a.com')
    print(friend1.getEmail())
    friend1.setEmailAddress('jagannath@gmail.com')
    print(friend1.getEmail())
    print(friend1)
    

#Initializa main function
if __name__=="__main__":
    main()
