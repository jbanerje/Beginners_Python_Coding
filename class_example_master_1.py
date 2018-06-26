class Clothing(object):
    #Description -  Clothing Class with Name and Cleanlines

    #Constructor
    def __init__(self,name,clean=True,times_worn=0,max_wears=2):
        self.name=name
        self.clean=clean
        self.times_worn = times_worn
        self.max_wears=max_wears

    #Accessor Methods(Getters)
    def getName(self):
        return self.name

    def isClean(self):
        return self.clean      

    #Mutator (Setters)
    def wear(self):
        self.times_worn += 1
        if self.times_worn >= self.max_wears:
            self.clean=False

    def wash(self):
        self.clean=True
        self.times_worn=0
        
    #String method
    def __str__(self):
        return "Clothing-"+self.name+" Clean-"+ str(self.clean)+ " times_worn-" + str(self.times_worn) + " max_wears-" + str(self.max_wears)
                 
def main():
    myJeans=Clothing("Blue Jeans",True)
    myShorts=Clothing("Shorts")
    myJeans.wear()
    print(myJeans)
    myJeans.wear()
    print(myJeans)
    myJeans.wash()
    print(myJeans)
    
if __name__=="__main__":
    main()
