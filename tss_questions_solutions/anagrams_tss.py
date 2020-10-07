word1 = "apple"
word2 = "aplpe"
word3="aple"
def solve(w1,w2):
	dct1={}
	dct2={}
	for ch in w1:
		if ch in dct1:
			dct1[ch]+=1
		else:
			dct1[ch]=1
	for ch in w2:
		if ch in dct2:
			dct2[ch]+=1
		else:
			dct2[ch]=1
	return dct1==dct2
print("ans=",solve(word1,word2))
print("ans=",solve(word1,word3))