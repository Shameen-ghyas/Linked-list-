class DLNode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    # function to insert a node to the right of the head
    def insert_right(self,value): 
        p=self
        q=DLNode(value)
        r=p.right
        p.right=q
        q.left=p
        q.right=r
        if r is not None:
            r.left=q
     # function to insert a node to the left of the head
    def insert_left(self,value):
        p=self
        q=DLNode(value)
        r=p.left
        q.right=p
        p.left=q
        q.left=r
        if r is not None:
            r.right=q 
    # function to delete a node
    def delete(self):
        p=self.left
        q=self
        r=self.right
        if p is not None:
            p.right=r
        if r is not None:
            r.left=p
        if p is None:
            return r
        return p
     
    #function to determine the length of a doubly linked list
    
    def __len__(self):
        a=self
        i=0
        while a is not  None:
            i+=1
            a=a.right
        a=self.left
        while a is not None:
            i+=1
            a=a.left
        return i 
    # function to traverse the whole list 
    def traverse(self):
        a=self
        while a.left is not None:
            a=a.left
        print("Traversing..")
        while a is not None:
            print(a.data,end='')
            a=a.right
        print()
    # function to search for a node 
    def search(self,target):
        b=self
        while b is not None and b.data!=target:
            b=b.right
        if b is not None:
            return b
        b=self.left
        while b is not None and b.data!=target:
            b=b.left
        return b 
    def __str__(self):
        # First, move to the leftmost node to start from the head of the list
        current = self 
        while current.left is not None:
           current = current.left
    
        # Traverse from the leftmost node and collect the data
        values = []
        while current is not None:
            values.append(str(current.data))  # Convert data to string
            current = current.right
    
        return " <-> ".join(values)
    
# function to convert the python list into doubly linked list and insert it to the right of the head
def build_list_right(val):
    assert len(val)>0,"no elements"
    a=DLNode(val[0])
    for i in range(1,len(val)):
        a.insert_right(val[i])
        a=a.right 
    return a 

# function to convert the python list into doubly linked list and insert it to the left of the head
def build_list_left(val):
    assert(len(val))>0,"no elements"
    a=DLNode(val[0])
    for i in range(1,len(val)):
        a.insert_left(val[i])
        a=a.left
    return a 

#function that accepts head pointer H to a doubly-linked list and inserts a node
#having info = x after the node with info = y.
def ins_D_list(H,x,y):
    a=H
    while a is not None and a.data!=y:
        a=a.right
    if a is not None:
        new=DLNode(x)
        new.left=a
        a.right=new 
    while a is not None and a.data!=y:
        a=a.left 
    new=DLNode(x)
    a.right=new
    new.left=a 

head=DLNode('a')
head.insert_right('b')
head.insert_left('c')
head.insert_left('d')
print(build_list_right(['e','f','h']))
print(build_list_left(['t','y','v']))
print(head)
