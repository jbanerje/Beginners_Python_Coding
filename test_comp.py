def comp(list1, list2):
    if  (( list1[0]== list2[0]) & ( list1[1]== list2[1]) & ( list1[2]== list2[2])):
        return 'true'
    else:
        return 'false'
        

list1=[1,2,4]
list2=[1,3,4]

result = comp(list1,list2)

print(result)

        

