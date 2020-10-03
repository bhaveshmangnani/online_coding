#User function Template for python3

def inPlace(root):
    #code here
    l = 0
    temp = root
    lst = []
    while temp:
        lst.append(temp.data)
        temp= temp.next
        l = l + 1
    temp = root
    for i in range(l//2):
        temp.data = lst[i]
        temp.next.data = lst[l-i-1]
        temp = temp.next.next

    if l%2:
        temp.data = lst[(l//2)]
    
    
    return root



#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def printList(head):
    tmp = head
    while tmp != None:
        print(tmp.data, end=" ")
        tmp = tmp.next
    print()


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n = int(input())
        arr = [int(x) for x in input().split()]

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)

        res = inPlace(ll.head)
        printList(res)
# } Driver Code Ends
