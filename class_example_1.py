class Employee:

    def __init__(self,firstName,lastName,eMail):
        self.firstName = firstName
        self.lastName = lastName
        self.eMail = eMail

emp1=Employee('Jagannath','Banerjee','jagannath.banerjee@gmail.com')
emp2=Employee('Roshni', 'Banerjee','roshni.banerjee22@gmail.com')

print(emp1.firstName,emp1.lastName,emp1.eMail)
