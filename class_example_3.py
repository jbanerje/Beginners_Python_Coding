# Jagannath Banerjee on 5/26/2017
#Class

class Employee:

    count=  0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.count  = Employee.count + 1
    
    def displayCount(self):
        print("Total Emp : ", Employee.count)

    def displayEmp(self):
        print('Name-',self.name , 'Salary-',self.salary)

emp_1 = Employee('Jagannath', 50000)
emp_2 = Employee('Roshni',60000)

emp_1. displayEmp()
emp_2. displayEmp()
print('Total Employee Count=',Employee.count)

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)
