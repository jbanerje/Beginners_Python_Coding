#python class

class Person:
    #constructor/initiliazor
    def __init__(self,name):
            self.name = name

    #method to return a string
    def whoami(self):
            return ("You are " + self.name)


p1 = Person('tom') # now we have created a new person object p1
print(p1.whoami())
print(p1.name)

p2 = Person('jerry') # now we have created a new person object p1
print(p2.whoami())
print(p2.name)
