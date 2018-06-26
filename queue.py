#Implementing queue

class queue:
    def __init__(self):
        self.item = []

    def isempty(self):
        return self.item == []

    def enque(self,item) :
        return self.item.insert(0,item)

    def dequeue(self,item):
        return self.item.pop()

    def size(self):
        return len(self.item)



    
q=queue()
q.enque(4)
q.enque("Dog")
q.enque(True)

print (q)
print (q.size())
