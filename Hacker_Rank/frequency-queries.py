#URL : https://www.hackerrank.com/challenges/frequency-queries/problem

def addKeyValue(dct, key, inc):
    if key in dct:
        dct[key] += inc
    else :
        dct[key] = inc
    return dct

def freqQuery(queries):
    
    dct ={}
    cntDct ={}
    i=1
    for _ in queries:
        cntDct[i] = 0
        i+=1
    
    ans = []
    for q in queries:
        
        q1, n1 = q
        #print("-"*10)
        #print("dct:",dct, "cnt", cntDct)
        if q1 == 1:
            if n1 in dct and dct[n1] in cntDct and cntDct[dct[n1]] > 0:
                cntDct = addKeyValue(cntDct, dct[n1], -1)
            dct = addKeyValue(dct, n1, 1)
            cntDct = addKeyValue(cntDct, dct[n1], 1)
        elif q1 == 2:
            if n1 in dct:
                cntDct = addKeyValue(cntDct, dct[n1], -1)
                if dct[n1] == 1:
                    del dct[n1]
                else :
                    dct[n1] -= 1
                    cntDct = addKeyValue(cntDct, dct[n1], 1)
        else:
            ans.append(1 if n1 in cntDct and cntDct[n1]>0 else 0)
    return ans
                    
                    
