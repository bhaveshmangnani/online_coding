def change_password(string, n, containsUpperCase, 
    containsLowerCase, containsDigit, containsSpecialChar):
        
        if(not containsUpperCase):
            string += 'A'
            n+=1
        if(not containsLowerCase):
            string += 'a'
            n+=1
        if(not containsDigit):
            string +='1'
            n+=1
        if(not containsSpecialChar):
            string += '#'
            n+=1
        if(n<7):
            string += 'a'*(7-n)
        return string
        
def validate_password(string, str_len):
    
    valid_length = str_len >= 7
    containsUpperCase = False
    containsLowerCase = False
    containsDigit = False
    containsSpecialChar = False
    
    specialChars = {'#', '@', '*', '&'}
    
    for i in range(str_len):
        
        if(not containsUpperCase and string[i] >= 'A' and string[i] <= 'Z'):
            containsUpperCase = True
        elif(not containsLowerCase and string[i] >= 'a' and string[i] <= 'z'):
            containsLowerCase = True
        elif(not containsDigit and string[i] >= '0' and string[i] <= '9'):
            containsDigit = True
        elif(not containsSpecialChar and string[i] in specialChars):
            containsSpecialChar = True
    
    return (valid_length and containsUpperCase and containsLowerCase and containsDigit and containsSpecialChar),valid_length, containsUpperCase, containsLowerCase, containsDigit, containsSpecialChar
    
    

tc = int(input())
for i in range(tc):
    
    n = int(input())
    string = input()
    
    isValidPassword, valid_length, containsUpperCase, containsLowerCase, containsDigit, containsSpecialChar = validate_password(string, n)
    
    if(not isValidPassword):
        string = change_password(string, n, containsUpperCase, 
    containsLowerCase, containsDigit, containsSpecialChar)
    
    print(f'Case #{i+1}: {string}')
    
    
    
    
    
