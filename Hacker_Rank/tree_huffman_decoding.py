#URL: https://www.hackerrank.com/challenges/tree-huffman-decoding/problem
def decodeHuff(root, s):
    #print(type(s))
    #Enter Your Code Here
    ans = ""
    node = root
    n = len(s)
    for i in range(n):
        side = s[i]
        
        if s[i]=="1":
            #print("in")
            if node.right:
                node = node.right
            else:
                #print("in1")
                ans =ans + node.data
                #print(ans)
                node = root.right
        else:
            if node.left:
                node = node.left
            else:
                ans+=node.data
                node = root.left
    ans+=node.data
    print( ans)
