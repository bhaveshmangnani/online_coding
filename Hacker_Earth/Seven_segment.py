n=int(input())
dct={'0':6,'1':2 , '2':5 , '3':5 , '4':4 , '5':5 , '6':6 , '7':3 , '8':7 , '9':6 }

for i in range(n):
    number=input()
    one_count=0
    seven_count=0
    for num in number:
        temp=dct[num]
        print(f"temp={temp}")
        if temp%2==0:
            temp=temp//2
            one_count+=temp
        else:
            seven_count+=1
            temp-=3
            temp=temp//2
            one_count+=temp

        print(f"temp={temp} one_count={one_count} seven={seven_count}")
    answer=''
    for j in range(seven_count):
        answer=answer+'7'
    
    for j in range(one_count):
        answer=answer+'1'
    
    print(answer)
