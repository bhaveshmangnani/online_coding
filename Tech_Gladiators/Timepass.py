a=[1,2,3,4,45,6]
for i in  a:
    print(i,"->",id(i))
    i=i+1

print("\n\n*****************************************\n\n")
for i in range(len(a)):
    print(a[i],"->",id(a[i]))



d={1:"BM",2:"BM10",3:"BM03"}
print("\n\n*****************************************\n\n")

for i in d.items():
    print(i,"->",id(i))


print(d.items())
print(type(d.items()))


"""
1 -> 140710003860304
2 -> 140710003860336
3 -> 140710003860368
"""
