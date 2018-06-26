class employee:
    def __init__(self,first,last,salary): # constructor
        self.first= first
        self.last= first
        self.pay= salary
        self.email= first +'.'+ last + '@gmail.com'

emp_1=employee('Jag','Banerjee',60000)
emp_2=employee('Rosh','banerjee',65000)

print(emp_1.email)
print(emp_2.email)

