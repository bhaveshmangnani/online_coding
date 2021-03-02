#URL: https://www.hackerrank.com/challenges/is-binary-search-tree/problem
def check_binary_search_tree_(root):
    
    def prefix(node):
        ans =[]
        if node.left:
            ans+=prefix(node.left)
        ans+=[node.data,]
        if node.right:
            ans+=prefix(node.right)
        return ans
    ans = prefix(root)
    return ans == sorted(set(ans))
