"""+20 13/2/2020,
+20 15/2/2020,
+30 19/2/2020,
+30 3/3/2020,
-40 25/3/2020,
+60 29/3/2020,
-40 10/4/2020,"""


def check_date_holding(date1, date2):
	#print(date1,date2,end="")
	d1 = date1[0]
	d2 = date2[0]
	if d1+30<=d2:
		return True
	if date2[1]>date1[1]+1: return True
	if date2[2]>date1[2]: return True
	months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
	td1 = d1
	d1 = (d1 +30)%( months[date1[1]])
	#print(d1,d2,end=" ")
	if d2>=d1 and date2[1]>date1[1]:
		return True
	return False




string = input("Enter transactions:\n")
new_trans = input("Enter new:\n")
if new_trans[0] =="+":
	print(True)
else:
	tns = string.split(",")
	holding = 30

	amt = []
	date=[]
	for t in tns:
		price,date_ = t.split()
		amt.append(int(price))
		
		d,m,y = date_.split("/")

		date.append([int(d),int(m),int(y)])
	for i in range(len(amt)):
		#print(amt[i],date[i])
		pass

	temp_amt ,new_date = new_trans.split()
	new_amt = -int(temp_amt)
	tn_date = [ int(x) for x in new_date.split("/") ]
	print(new_amt,tn_date)
	
	n = len(amt)
	allowed = 0
	for i in range(n):
		#print(check_date_holding(date[i], tn_date))
		if check_date_holding(date[i], tn_date) or amt[i]<0:
			allowed += amt[i]
	print("allowed=",allowed)
	print("ANS=",end="")
	if allowed>=new_amt:
		print(True)
	else:
		print(False)


	


