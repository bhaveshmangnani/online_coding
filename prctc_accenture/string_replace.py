string = input("Enter string: ")
string1 = list(string)
ch1 = input("Enter ch1: ")
ch2 = input("Enter ch2: ")

string = string.replace(ch1,"*").replace(ch2,ch1).replace("*",ch2)
print(string)



indices = []
for i in range(len(string)):
    if string1[i]==ch1:
        indices.append(i)
    elif string1[i]==ch2:
        string1[i]=ch1

for i in indices:
    string1[i]=ch2
print("my", "".join(string1))
