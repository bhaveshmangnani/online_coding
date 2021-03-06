import math

def is_operand(ch):
    if ch.isdecimal():
        return True
    return False

def priority(operator):
    dct = {'(':0,')':0, '+':1 , '-':1,'*':2,'/':2,'^':3,"$":4}
    return dct[operator]

def in_to_post(s):
    stack = [ ]
    top = -1
    ops =[ ]
    for i in s:
        if i =="log":
            i="$"
        #print("in",i)
        if is_operand(i):
            ops.append(i)
        elif i =='(':
            stack.append(i)
            top =top +1
        else:
            if stack:
                while top>-1 and (priority(stack[top])>=priority(i)):
                    tops=stack.pop()
                    top = top -1
                    if tops != '(':
                        ops.append(tops)
                    else :
                        break
                if i!=')':
                    stack.append(i)
                    top = top+1
            else:
                stack.append(i)
                top+=1
    if stack:
        for i in range(top+1):
            ops.append(stack.pop())
            top = top -1

    return ops

string = input("infix").split()

def solve(num1,num2,op):
	num1=float(num1)
	num2=float(num2)
	dct = {
		"+":num1+num2,
		"-":num1-num2,
		"*":num1*num2,
		"/":num1/num2
	}
	return dct[op]

def eval_post(lst):
	post=in_to_post(lst)
	stack = []
	top = -1
	for i in post:
		#print(stack)
		if i.isalnum():
			stack.append(i)
		else:
			if  i =="$":
				num = stack.pop()
				top-=1
				stack.append(math.log(num))
			else:
				num2=stack.pop()
				top-=1
				num1=stack.pop()
				top-=1
				stack.append( solve(num1,num2,i) )
				top+=1
	return stack[0]
			

print("postfix="," ".join(in_to_post(string)))
#print("ans=",eval_post(string))

