word = "AABBCCCDDEEFFAABBC"
def solve(word):
	n=len(word)
	ans=""
	i=0
	j=0
	while i<n:
		tempcount=1
		ch=word[i]
		j=i+1
		while j<n and word[j]==word[j-1]:
			tempcount +=1
			j+=1
		ans = ans + str(tempcount)+ch
		i=j
	return ans
print("ans=",solve(word))
