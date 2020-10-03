#User function Template for python3

# Linked List Node Structure

class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, data):
        if self.head ==None:
            self.head = Node(data)
        elif data ==0:
            ts = Node(data)
            ts.next = self.head
            self.head = ts
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
    
    # Move Zeros to the front of the list
    def moveZeroes(self):
         ts = self.head
         while ts and ts.data ==0:
             ts=ts.next
         
             
         
         
         
     
    def display(self):
        temp = self.head
        while temp and temp.data==0:
            print(temp.data,end=" ")
            temp = temp.next
        
        lst = []
        while temp:
            lst.append(str(temp.data))
            temp = temp.next
        for i in lst[::-1]:
            print(i,end =" " )
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        lis = LinkedList()
        n = int(input())
        arr = list(map(int, input().strip().split()))
        #head = createList(arr, n)
        for i in range(0,len(arr)):
            lis.push(arr[i])
        lis.moveZeroes()
        lis.display()
        print()
# } Driver Code Ends
