#URL : https://www.hackerrank.com/challenges/sherlock-and-anagrams
def sherlockAndAnagrams(s):
    # Write your code here
    
    n = len(s)
    dct = {}
    count = 0
    
    for i in range(n):
        for j in range(i,n):
            substring = s[i:j+1]
            #print(f"i = {i} j = {j} k = {k}")
            #print(f"strt = {k} end = {i+1} ss = {substring}")
            ss = "".join(sorted(substring))
            if ss in dct:
                dct[ss] += 1
            else:
                dct[ss] = 1
                #print(dct)

    for key in dct.keys():
        val = dct[key]
        count += (val*(val-1))//2
    return count
    
