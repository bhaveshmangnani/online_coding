#URL: https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem?h_r=profile

def lca(root, v1, v2):
  #Enter your code here
  s1 = []
  n = 0
  node = root
  while node:
    
    s1.append(node)
    n+=1
    if v1>node.info:
        node = node.right
    elif v1<node.info:
        node = node.left
    else:
        break
    
  s2 = []
  m = 0
  node = root
  while node:
    
    s2.append(node)
    m+=1
    if v2>node.info:
        node = node.right
    elif v2<node.info:
        node = node.left
    else:
        break
  ans = root
  for i in range(min(m,n)):
    if s1[i].info!=s2[i].info:
        break
    ans = s1[i]
  return ans
