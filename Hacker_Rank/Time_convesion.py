str1=input()
temp=str1[8:]
str1=str1[0:8]

time=[int(x) for x in str1.split(":")]



if time[0]>=0 and  time[0]<24:
    if time[1]>=0 and time[1]<60:
        if time[2]>=0 and time[2]<60:
                if temp.lower() =='pm':
                    if time[0]==12:
                        print(str1)
                    else:
                        print( str((int(str1[0:2])+12)%24) +str1[2:] )
                else:
                    if time[0]==12:
                        print("00"+str1[2:])
                    else:
                        print(str1)