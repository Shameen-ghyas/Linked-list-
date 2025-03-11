#Queue ADT using python list
class Queue:
    def __init__(self):
        self.__qlist=list()

    #checks whether the queue is empty or not 
    def isEmpty(self):
        return len(self)==0
    
    #returns the length of the queue
    def __len__(self):
        return len(self.__qlist) 
    
    #append an item to the queue
    def enqueue(self,item):
        self.__qlist.append(item)
    
    #removes and returns the fisrt item in the queue
    def dequeue(self):
        assert not self.isEmpty(),"cannot dequeue from an empty queue"
        return self.__qlist.pop(0)
    
    #prints the queue
    def print_queue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            for item in self.__qlist:
                print(item,end=' ')
            print()


    
Q=Queue()
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)
Q.enqueue(6)
Q.enqueue(7)
Q.print_queue()
Q.dequeue()
Q.print_queue()

#Circular Queue using Array 

import ctypes


class Array:
    def __init__(self, n):
        assert n > 0, 'Array size must be > 0'
        self.size = n
        self.elements = (ctypes.py_object * n)()
        self.clear(None)

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        assert index >= 0 and index < len(self), "Invalid index"
        return self.elements[index]

    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), "Invalid index"
        self.elements[index] = value

    def insert(self, index, value):
        print(self.size)
        for i in range(self.size - 1, index, -1):
            self.elements[i] = self.elements[i-1]
        self.elements[index] = value

    def delete(self, index):
        for i in range(index, self.size-1, 1):
            self.elements[i] = self.elements[i + 1]
        self.elements[self.size-1] = None

    def traverse(self):
        for i in range(len(self)):
            print(self.elements[i], end=" ")
        print()

    def clear(self, value):
        for i in range(len(self)):
            self.elements[i] = value

class Circular:
    def __init__(self,maxsize):
        self.front=0
        self.back=maxsize-1
        self.count=0
        self.qArray=Array(maxsize)

    def isEmpty(self):
        return self.count==0
    
    def isFull(self):
        return self.count==len(self.qArray)
     
    def __len__(self):
        return self.count
    def enqueue(self,item):
        assert not self.isFull(),"cannot enqueue to a full queue"
        maxsize=len(self.qArray)
        self.back=(self.back+1) % maxsize
        self.qArray[self.back]=item 
        self.count+=1
    
    def dequeue(self):
        assert not self.isEmpty(),"cannot dequeue from an empty queue"
        item=self.qArray[self.front]
        maxsize=len(self.qArray)
        self.front=(self.front+1) % maxsize 
        self.count-=1
        return item 
    
    def traverse(self):
        self.qArray.traverse()

C=Circular(5)
C.enqueue(4)
C.enqueue(34)
C.enqueue(32)
C.enqueue(15)
C.enqueue(78)
C.traverse()
C.dequeue()
C.traverse()
C.enqueue(89)
C.traverse()
print(C.count)

#Priority Queue
class _PriorityQEntry:
    def __init__(self,item,priority):
        self.item = item
        self.priority=priority
class PriorityQueue:
    def __init__(self):
        self.qList=list()
    def isEmpty(self):
        return len(self.qList)==0
    
    def enqueue(self,item,priority):
        entry=_PriorityQEntry(item,priority)
        self.qList.append(entry)
    
    def dequeue(self):
        assert not self.isEmpty(),"cannot dequeue from an empty queue"
        highest_index = 0
        highest_priority=self.qList[0].priority
        for i in range(1,self.len()):
            if self.qList[i].priority<highest_priority:
                highest_priority=self.qList[i].priority 
                highest_index=i
        entry=self.qList.pop(highest_index)
        return entry.item
    
    def len(self):
        return len(self.qList)
    
    def enqueue1(self,item,priority):
        entry=_PriorityQEntry(item,priority)
        inserted=False
        for i in range(self.len()):
            if self.qList[i].priority>priority:
                self.qList.insert(i,entry)
                inserted=True
                break 
        if not inserted:
            self.qList.append(entry)
        
        return self.qList 
    
    def __str__(self):
        return ','.join(f'({entry.item},{entry.priority})' for entry in self.qList)
    
# p=PriorityQueue()
# p.enqueue1('black',4)
# p.enqueue1('blue',0)
# p.enqueue1('green',3)
# p.enqueue1('purple',7)
# p.enqueue1('red',1)
# print(p)
# p.dequeue()
# print(p)
# p.dequeue()
# print(p)
# p.dequeue()
# print(p)
# p.dequeue()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Circular_Queue:
    def __init__(self):
        self.front=None
        self.back=None
    def isEmpty(self):
        return self.front is None
    def enqueue(self,x):
        new_node=Node(x)
        if self.isEmpty():
            self.front=new_node
            self.back=new_node

            self.back.next=self.front
        else:
            self.back.next=new_node
            self.back=new_node
            self.back.next=new_node 
        print(f'enqueued {x}')
    
    def dequeue(self):
        if self.isEmpty():
            print("cannot dequeue")
            return None 
        del_item=self.front.data
        if self.front==self.back:
            self.front=self.back = None
        else:
            self.front = self.front.next 
            self.back.next=self.front 
        print("dequeued",del_item)
        return del_item
    def traverse(self):
        current=self.front
        while current!=self.back:
            print(current.data)
            current=current.next
        print(current.data)
        
x=Circular_Queue()
x.enqueue(4)
x.enqueue(3)
x.enqueue(2)
x.traverse()

