#Matplotlib -  Pie Chart

#Import Library
import matplotlib.pyplot as plt

#Main Function
def main():
    print("hello")
    gases=['nitrogen','oxygen','argon','hydrogen']
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    #fig1, ax1 = plt.subplots()
    plt.pie(sizes, explode=explode, labels=gases, autopct='%1.1f%%',shadow=True, startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
    
if __name__=="__main__":
    main()
