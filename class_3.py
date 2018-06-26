# -*- coding: utf-8 -*-

"""
Created on Fri Nov 24 12:08:30 2017
OOP-3
@author: jagan
"""
class Clothing(object):
    #Explanation - Its a clothing class defining a pice pf clothing
    
    #Constructor(Initialization)
    def __init__(self,name,clean=True,times_worn=0,max_wear=1):
        self.name = name
        self.clean = clean
        self.times_worn=times_worn
        self.max_wear=max_wear
        
    #Getters(Accesors Method)
    def getName(self):
        return self.name
    
    def isClean(self):
        return self.clean
    
    def wear(self):
        self.times_worn +=1
        if (self.times_worn > self.max_wear) :
            self.clean=False
            
    def wash(self):
            self.clean=True
            self.times_worn=0
    
    #Setters(Mutators Method)
    
    
    #def String to print friend1. This is inherited from object class
    def __str__(self):
        return "Clothing[" + " Name:"+self.name+" Clean:"+str(self.clean)+ " Times_Worn:"+str(self.times_worn) + " Max wear:"+str(self.max_wear) + "]"

class Shirt(Clothing):  #Inheritence
    
#Constructor(Initialization)
    def __init__(self,name,clean=True,times_worn=0,max_wear=1,shortSleeves=True):
        
        #initializing the instance variables
        super().__init__(name,clean=True,times_worn=0,max_wear=1)
        
        self.shortSleeves=shortSleeves
        
    #Getters(Accesors Method)
    def hasShortSleeves(self):
        return self.shortSleeves
    
    #def String to print friend1. This is inherited from object class
    def __str__(self):
        return "Shirt[" + super().__str__() + " Short Sleeves "+ str(self.shortSleeves) + "]"
    
#Main Function
def main():
    myClothes=[]
    myClothes.append(Clothing('Ble Jeans',False))
    myClothes.append(Clothing('Cap',True,20,100))
    myClothes.append(Clothing('Jacket',True,20,100))
    myClothes.append(Shirt('T-Shirt',True,0,1))
    myClothes.append(Shirt('Shirt',True,0,1,False))
    
    print("\n ========Full Wardrobe================")
    
    for i in range(len(myClothes)):
        print(myClothes[i])
        
    print("\n ========Clean Clothes================")
    for i in range(len(myClothes)):
        if myClothes[i].isClean():
            print(myClothes[i])
    
    print("\n ========Dirty Clothes================")
    for i in range(len(myClothes)):
        if not myClothes[i].isClean():
            print(myClothes[i])
    
    print("\n ========Shirts================")
    for i in range(len(myClothes)):
        if isinstance(myClothes[i],Shirt):
            print(myClothes[i])  
    
    print("\n ========Clean Shirts Only================")
    myClothes[4].wear()
    for i in range(len(myClothes)):
        if isinstance(myClothes[i],Shirt):
            if myClothes[i].isClean():
                print(myClothes[i]) 
    

#Initializa main function
if __name__=="__main__":
    main()
