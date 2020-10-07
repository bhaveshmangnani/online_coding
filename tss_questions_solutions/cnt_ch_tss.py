word = "AABBCCCDDEEFFAABBC"
def solve(word):
	ans=""
	n=len(word)
	ch=word[0]
	pos=None
	cnt_ch=1
	for i in range(n):
		if ch!=word[i]:
			ans = ans + str(cnt_ch)+ch
			ch = word[i]
			cnt_ch=1
			pos=i
		else:
			cnt_ch+=1
	ans=ans+str(n-pos-1)+word[n-1]
	
print("ans=",solve(word))
