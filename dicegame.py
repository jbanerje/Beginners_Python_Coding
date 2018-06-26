#Dice Rolling simulator

import random
import sys
import os
import matplotlib


random_num = random.randrange(1,6)

print('*----------------------------*')
print('    Welcome to the Dice Game')
print('*----------------------------*')
print('Ok the game starts.....')
userInput = "y"
while(userInput != "n"):
       print 'Your # is :', random_num
       random_num = random.randrange(1,6)
       userInput = input("Roll the dice (y/n)? ")
print('*----------------------------*')       
print('Thanks for playing dice!')
print('*----------------------------*')