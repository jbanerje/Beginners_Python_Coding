#OOP

def main():

    friends=[]

    for i in range(2):
        name=input('Enter Name:')
        phone=input('Phone:')
        email=input('Email:')
        friends.append([name,phone,email])

    print(friends)
    
    for friends_counter in range(len(friends)):
        print("Contact Info:")
        for contact_counter in range(len(friends[friends_counter])):
            print(friends[friends_counter][contact_counter])

if __name__=="__main__":
    main()
