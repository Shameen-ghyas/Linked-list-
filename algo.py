
class ListNode:
      def __init__(self,val):
            self.data=val
            self.next=None
      def insert(self,value):
            n=ListNode(value)
            n.next=self.next
            self.next=n
            return n
      def insert_at_end(self,value):
            n=ListNode(value)
            a=self
            while a.next is not None:
                 a=a.next
            a.next=n
      def delete(self):
            item=0
            if self.next is not None:
                tmp=self.next
                self.next=tmp.next
                item=tmp.data
            return item
      def search(self,target):
            a=self
            if a.data==target:
                 return [True,None,a]
            b=a.next
            while b is not None and b.data!=target:
                 a=a.next
                 b=b.next
            return [b is not None,a,b]
     
    

      def del_new(self, val):
        # Handle the case where the head node(s) contain the value to delete
        while self is not None and self.data == val:
            self = self.next  # Move head to the next node if it matches the value

        current = self  # Start traversing from the new head
        while current is not None and current.next is not None:
            if current.next.data == val:
                current.next = current.next.next  # Skip the node with the matching value
            else:
                current = current.next  # Move to the next node

        return self  # Return the updated list with the new head

      def __str__(self):
        current = self
        values = []
        while current is not None:
            values.append(current.data)
            current = current.next
        return " -> ".join(values)

def insafter(head,x,val):
     res=head.search(x)
     if res[0]==True:
          res[2].insert(val)

def insbefore(head,x,val):
     res=head.search(x)
     if res[0]==True:
            if res[2] is head:
               new=ListNode(val)
               new.next=head
               head=new
            else:
               res[1].insert(val)
     return head

def delnode(head,x):
      res=head.search(x)
      if res[0]==True:
            if res[2] is head:
                 head=head.next
            else:
                 res[1].delete()
      return head
class DLL:
     def __init__(self,val):
       self.data=val 
       self.right=None
       self.left=None
     def __str__(self):
        result = []
        current = self
        while current is not None:
            result.append(str(current.data))  # Append the data to the result list
            current = current.next  # Move to the next node
        return " <-> ".join(result)


def buildlist():
      val=[]
      while True:
        n=input("enter the value orr press 'y' to quit:")
        if n.lower() =='y':
            break 
        val.append(n)
        a=ListNode(val[0])
        b=a
        for i in range(1,len(val)):
            new=ListNode(val[i])
            new.next=b.next
            b.next=new
            b=b.next 
      return a
def del_x(H,x):
      a=H
      b=a.next
      if H is None:
           return None
      if H is not None and H.data==x:
           H=H.next
      while b is not None:
           if b.data==x:
                a=b.next
                b=b.next
           b=b.next 
           a=a.next
      return H 


def count_x(H,x):
      i=0
      a=H
      if a is None:
          return 0
      while a is not None:
          if a.data==x:
               i+=1
          a=a.next
      return i
def del_tail(H):
      a=H
      if a is None:
          return None
      while a.next.next is not None:
           a=a.next
      a.next=None
      return H
def combine(l1,l2):
     a=l1
     b=l2
     if a is None:
          return b
     elif b is None:
          return a
     while a.next is not None:
          a=a.next
     a.next=b
     return l1

def split(head):
     a=head
     if a is None:
          return None
     
     while a.next is not None:
          if int(a.data) <0:
               second_list=a.next
               a.next=None
               return [head,second_list]
          a=a.next
     # a=a.next
     return [head,second_list]

def insB4tail(H,x):
     a=H
     if a.next is None:
          return None
     while a.next.next is not None:
          a=a.next
     a.insert(x)
     return H

def newHead(H,x):
     a=H
     if a is None:
          return None
     if a.data==x:
          return H
     # b=None
     while a.next is not None:
          if a.data==x:
               return a
          # b=a
          a=a.next 
     # return None
def insafterDlst(H,x,y):
     p=H
     q=DLL(x)
     r=p.right
     r.data=y
     p.right=q
     q.left=p
     q.right=r
     if r is not None:
          r.left=q

def search(H,x):
     a=H
     b=a.next
     if H is None:
          return None
     if H.data==x:
          return [True,None,H]
     while b is not None and b.data!=x:
          a=a.next
          b=b.next
     return [b is not None,a,b]

def ins_after(H,x,val):
     a=H
     b=a.next
     if H is None:
          new=ListNode(val)
          return new
     if H is not None and H.data==x:
            new=ListNode(val)
            new.next=H.next
            H.next=new
            return H
     while b is not None:
          if b.data==x:
                new=ListNode(val)
                new.next=b.next
                b.next=new 
          a=a.next
          b=b.next
     return H
def ins_b4(H,x,val):
     a=H
     b=a.next
     if H is None:
          new=ListNode(val)
          return new
     if H is not None and H.data==x:
            new=ListNode(val)
            new.next=H
          #   H.next=new
            return new
     while b is not None:
          if b.data==x:
                new=ListNode(val)
                new.next=b
                a.next=new 
          a=a.next
          b=b.next
     return H
def circularize(H):
     a=H
     while a.next is not None:
          a=a.next
     a.next=H
     return H

def insClist(H,y,x):
     a=H
     b=a.next
     if a is None:
          return None
     if b is not H and b.data==y:
          new=ListNode(x)
          new.next=b.next
          b.next=new
          return H
     while b is not H and b.data!=y:
          b=b.next
          a=a.next
     if b is H:
          return None 
     new=ListNode(x)
     new.next=b.next
     b.next=new
     return H


def bubblesort(H):
     if H is None:
          return None
     if H.next is None:
          return None
     a=H
     while a.next is not None:
          b=a
     
          while b.next is not None:
            if b.data>b.next.data:
               tmp=b.data
               b.next.data=tmp
               b.data=b.next.data
            b=b.next 
     return H


      

head=ListNode('2')
head.insert('4')
head.insert('3')
# head.insert('d')
# head.insert('e')
# head.insert('f')
# head.insert('g')
# # print(circularize(head))
# print(insClist(head,'d','6'))
# print(ins_b4(head,'d','6'))
# print(ins_after(head,'d','j')) 
# print(insbefore(head,'b','c'))
# insafter(head,'b','c')
# print(del_x(head,'d'))
# head.del_new('d')
# print(head.search('c'))
print(head)


# print(insB4tail(head,'x'))
# head.delete()

head2=ListNode('9')
head2.insert('4')
head2.insert('6')
# print(bubblesort(head2))
# print(del_x(head,'c'))
print(head2)
# print(combine(head,head2))
# print(buildlist())
# print(newHead(head,'c'))
# head3=buildlist()
# print(split(head3))
# print(count_x(head,'c'))
# print(del_tail(head))
# print(delnode(head,'c'))
# print(head)
# h=DLL('f')
# print(insafterDlst(h,'c','a'))
def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a=l1
        b=l2
        lst=[]
        s=''
        t=''
        while a:
            s+=str(a.data)
            a=a.next 
        while b:
            t+=str(b.data)
            b=b.next
        s=int(s)
        t=int(t)
        sum_=s+t
        sum_=str(sum_)
        store=sum_.split()
        head=ListNode(int(store[0]))
        x=head
        for i in range(1,len(store)):
            new_node=ListNode(int(store[i]))
            x.next.insert(new_node)
        return head
print(addTwoNumbers(head,head2))  