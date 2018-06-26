import random
import sys
import os
import matplotlib.pyplot as pt

#Simple graph by reading a file
x=[]
y=[]

readfile = open("C:\\Users\\Jagannath\\Desktop\\Python\\coordinate.txt","r")
data = readfile.read().split("\n")

for i in data:
    val = i.split(",")
    x.append(int(val[0]))
    y.append(int(val[1]))
    
pt.plot(x,y)
pt.show()
pt.title ("Rain in December")
pt.xlabel("Days in December")
pt.ylabel("Inches")
