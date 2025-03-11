#implementing stack ADT using python list
class stack:
    def __init__(self):
        self.elements=list()
    def isEmpty(self):
        return len(self.elements)==0
    def pop(self):
        assert not self.isEmpty(),"cannot pop from an empty stack"
        x=self.elements.pop()
        return x 
    def push(self,val):
        self.elements.append(val)

#implementing function to conert infix expression to postfix 
# function to check precedence 
def precedence(x):
    if x=='{' or x=='[' or x=='(':
        return 0
    if x=="+" or x== "-":
        return 1
    if x=='*' or x=='/':
        return 2
    else:
        return 3 
    
def a_higher_b(a,b):
    return precedence(a)>precedence(b)

def infix_to_postfix(expr):
    st=stack()
    postfix=[]
    for i in range(len(expr)):
        token=expr[i]
        if token=='{' or token=='[' or token=='(':
            st.push(token)
        elif  token=='}' or token==']' or token==')':
            flag=False
            while not flag:
                if not st.isEmpty():
                    top=st.pop()
                    postfix.append(top)
                    if top=='{' or top=='[' or top=='(':
                       flag =True
                    else:
                        postfix.append(token)
                else:
                    flag = True 
        elif token == "^" or token == "+" or token == "-" or token == "*" or token == "/":
            flag= False 
            while not flag:
                if st.isEmpty():
                   st.push(token)
                   flag = True 
                else:
                    top=st.pop()
                    if a_higher_b(token,top):
                        st.push(token)
                        flag = True 
                    else:
                        postfix.append(top)
        else:
            postfix.append(token)
    while not st.isEmpty():
        top=st.pop()
        postfix.append(top)
    return postfix         

def evaluate(expr):
    st=stack()
    for i in range(len(expr)):
        token=expr[i]
        if token=='^' or token=='*' or token=='/' or token=='+' or token=='-':
            val2=st.pop()
            val1=st.pop()
            if token=='^':
                res=pow(val1,val2)
            elif token=='*':
                res=val1*val2
            elif token=='/':
                res=val1//val2 #we are working with integer math
            elif token=='+':
                res=val1+val2
            else:
                res=val1-val2
            st.push(res)
        else:
            st.push(token)
    return res


myinfix=[2,'*',5,'+',7,'+','{',3,'^',2,'*',4,'+',5,'-',1,'}','*',3]
print("infix=",myinfix)
mypostfix=infix_to_postfix(myinfix)
print(mypostfix)
value=evaluate(mypostfix)
print("value=",value)

def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1 

def quick_sort(arr):
    s=stack()
    s.push((0,len(arr)-1))
    while not s.isEmpty():    
        low,high=stack.pop()
        pivot_indexes=partition(arr,low,high)
        if low<pivot_indexes -1:
            s.push(low,pivot_indexes-1)
        if pivot_indexes+1<high:
            s.push(pivot_indexes+1,high)
