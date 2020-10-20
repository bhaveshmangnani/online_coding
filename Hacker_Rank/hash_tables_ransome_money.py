#URL: https://www.hackerrank.com/challenges/ctci-ransom-note/problem

def checkMagazine(m, n, magazine, note):
    mdct = {}
    for word in magazine:
        if word in mdct:
            mdct[word]+=1
        else:
            mdct[word]=1
    
    for word in note:
        occ = mdct.get(word,0)
        if not occ:
            print("No")
            break
        else:
            mdct[word]-=1
    else:
        print("Yes")
