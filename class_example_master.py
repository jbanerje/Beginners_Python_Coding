#OOP

class Person(object):
    
    #The Person class defines a person with name,phone and email

    #Constructor
    def __init__(self,name,phone,email):   #self refers to the object itself 
        self.name=name  #instance variable
        self.phone=phone
        self.email=email

    #Accessor Methods(Getters)

    def getName(self):
        return self.name

    def getPhone(self):
        return self.phone

    def getEmail(self):
        return self.email

    #Mutator (Setters)

    def setPhone(self,newPhoneNumber):
        self.phone=newPhoneNumber

    def setEmail(self,newemailAdd):
        self.email=newemailAdd

    def __str__(self):
        return "Person[name= " + self.name
        
def main():

    friend1=Person('Jag',111,'a@a.com') #Instance of class
    friend2=Person('Tom',222,'b@b.com') #Instance of class
    friend3=Person('Har',333,'c@c.com') #Instance of class

    print(friend1.getEmail())
    friend1.setEmail('jagannath.banerjee@gmail.com')
    print(friend1.getEmail())
    print(friend1)
    
if __name__=="__main__":
    main()

#Object - Container that can manager data
# Person

