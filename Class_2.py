# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 12:41:11 2017

@author: jagan
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 12:08:30 2017
OOP-1
@author: jagan
"""
class Clothing(object):
    #Explanation - Its a clothing class defining a pice pf clothing
    
    #Constructor(Initialization)
    def __init__(self,name,clean=True):
        self.name = name
        self.clean = clean
        
    #Getters(Accesors Method)
    def getName(self):
        return self.name
    
    def isClean(self):
        return self.clean
    
    #Setters(Mutators Method)
    
    
    #def String to print friend1. This is inherited from object class
    def __str__(self):
        return "Clothing[" + " Name:"+self.name+" Clean:"+str(self.clean)+"]"
        
#Main Function
def main():
    #print("Hello")
    myJeans=Clothing('Ble Jeans',False)
    myShorts=Clothing('Shorts')
    
    #print(myJeans.getName())
    #print(myShorts.isClean())
    print (myJeans)
    print (myShorts)
    

#Initializa main function
if __name__=="__main__":
    main()
