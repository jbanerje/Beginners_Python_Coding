#Kaggle Script with python
import matplotlib.pyplot as plt
import csv as csv
import numpy as np

# initialize variabes
csvdata=[]                          
maleCount = 0
femaleCount = 0
index = 0
maleClass1 = 0
maleClass2 = 0
maleClass3 = 0

femaleClass1 = 0
femaleClass2 = 0
femaleClass3 = 0

# Open up the csv file in to a Python object
csv_file_object = csv.reader(open('C:\\Users\\Jagannath\\Desktop\\Python\\train.csv', 'r')) 
header = csv_file_object.next()  # The next() command just skips the 
                                 
#Copy csv file into the list csvdata
for row in csv_file_object:      
    csvdata.append(row)
              
data = np.array(csvdata) 	

#Getting the male/female count
for index in range(len(csvdata)):
    if (data[index,4] == "male"):
        maleCount = maleCount + 1
        if (data[index,2] == "1"):
            maleClass1 = maleClass1 + 1
        elif (data[index,2] == "2"):
            maleClass2 = maleClass2 + 1
        else:
            maleClass3 = maleClass3 + 1
            
    else:
        femaleCount = femaleCount + 1
        if (data[index,2] == "1"):
            femaleClass1 = femaleClass1 + 1
        elif (data[index,2] == "2"):
            femaleClass2 = femaleClass2 + 1
        else:
            femaleClass3 = femaleClass3 + 1

print "Male_Count  : ", maleCount , ":",maleClass1,":",maleClass2,":",maleClass3
print "Female_Count: ",femaleCount, ":",femaleClass1,":",femaleClass2,":",femaleClass3

#Creating a Pie Chart
fig = plt.figure()
rect = fig.patch
rect.set_facecolor('green')
graph1 = fig.add_subplot(2,2,1,axisbg='black')

#Value of pie
sizes = [maleCount,femaleCount]
colors = ["magenta", "red"]
labels = ['Male','Female']

plt.pie(sizes,colors=colors,startangle=90,labels=labels)

#Adding labels to pie chart
plt.title('Male/Female Count in Titanic')
#plt.legend(title='Legend', loc='lower left')
plt.axis('equal')
plt.show()

#bar chart
graph2 = fig.add_subplot(2,2,2,axisbg='black')
PassClass = 3
malesClass = (maleClass1, maleClass2, maleClass3)
femalesClass = (femaleClass1, femaleClass2, femaleClass3)

ind = np.arange(PassClass)    # the x locations for the groups
width = 0.20       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, malesClass, width, color='r')
p2 = plt.bar(ind, femalesClass, width, color='y',bottom=malesClass)

plt.ylabel('# of Passengers')
plt.title('Male Female in each class')
plt.xticks(ind + width/2., ('Class_1', 'Class_2', 'Class_3'))
plt.yticks(np.arange(0, 500, 100))
#plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()



