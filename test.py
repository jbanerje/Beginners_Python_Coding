print("======================Python Test=================================")
print("Hello World!")
var1=5+5
print (var1)
counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print (counter)
print (miles)
print (name)

#Python Strings
print("======================Python String=================================")
str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

#Python Lists
print("======================Python List=================================")
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)          # Prints complete list
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd 
print (list[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list + (tinylist)) # Prints concatenated lists

#Python Lists
print("======================Python Tuples=================================")
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)           # Prints complete list
print (tuple[0])        # Prints first element of the list
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print (tuple[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints list two times
print (tuple + tinytuple) # Prints concatenated lists

#Time
print("======================Python Time=================================")
import time;
localtime = time.localtime(time.time())
print ("Local current time :", localtime)

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

#Calender
print("======================Python Calender=================================")
import calendar

cal = calendar.month(2016, 6)
print ("Here is the calendar:")
print (cal)
