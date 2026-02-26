# 1 : define 8 fns (trapping conditions for checking password)

def no_lowercase(pw) : # return T/F
    for i in range(len(pw)) :
        # check if any string in uppercase
        if pw[i] in 'abcdefghijklmnopqrstuvwxyz' :
            return False
    # end loop -> if not return False first , return True instead
    return True
    
def no_uppercase(pw) : # return T/F
    for i in range(len(pw)) :
        # check if any string in uppercase
        if pw[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' :
            return False
    # end loop -> if not return False first , return True instead
    return True

def no_number(pw) :
    for i in range(len(pw)) :
        # check if any string in number
        if pw[i] in '0123456789' :
            return False
    # end loop -> if not return False first , return True instead
    return True

def no_symbol(pw) :
    for i in range(len(pw)) :
        # check if any string in number
        if pw[i] in ':<>?!@#$%^&*(.);{}[]"\'' :
            return False
        # end loop -> if not return False first , return True instead
    return True

def character_repetition(pw) :
    for i in range(len(pw) - 3) : # -3 for checking 3 next
        if pw[i] == pw[i+1] == pw[i+2] == pw[i+3] :
            return True
    # if not character repetition -> return F
    return False

def number_sequence(pw) :
    for i in range(len(pw) - 3) : # -3 for checking 3 next
        if (pw[i:i+4] in '01234567890') or (pw[i:i+4] in '09876543210') :
            return True
    return False # return F if not in num seq 
                
def letter_sequence(pw) :
    for i in range(len(pw) - 3) : # -3 for checking 3 next
        if (pw[i:i+4].lower() in 'xyzabcdefghijklmnopqrstuvwxyz') \
           or (pw[i:i+4].lower() in 'zyxwvutsrqponmlkjihgfedcbazyx'):
            return True
    return False # return F if not in letter seq

def keyboard_pattern(pw) :
    for i in range(len(pw) - 3) : # -3 for checking 3 next
        if (pw[i:i+4].upper() in '!@#$%^&*()_+QWERTYUIOPASDFGHJKLZXCVBNM') \
           or (pw[i:i+4].upper() in 'MNBVCXZLKJHGFDSAPOIUYTREWQ+_)(*&^%$#@!') :
            return True
    return False # if cant find keyboard pattern

# -----------------------------------------------------
password = input().strip() # for special char.
errors = []

# consider all cases by calling 8 trapped function (6 tasks) -> if dont meets cd. , append error

# case 1 : length > 8
if len(password) < 8 :
    errors.append('Less than 8 characters')
    
# case 2 : have upper,lower,number,symbol -> if fn = True
if no_lowercase(password) == True :
    errors.append('No lowercase letters') 
        
if no_uppercase(password) == True :
    errors.append('No uppercase letters')

if no_number(password) == True :
    errors.append('No numbers')

if no_symbol(password) == True :
    errors.append('No symbols')

# case 3 : no need character repetition
if character_repetition(password) == True :
    errors.append('Character repetition')
    
# case 4 : no need number sequence 
if number_sequence(password) == True :
    errors.append('Number sequence')
 
# case 5 : no need letter sequence 
if letter_sequence(password) == True :
    errors.append('Letter sequence')
    
# case 6 : no need keyboard pattern 
if keyboard_pattern(password) == True :
    errors.append('Keyboard pattern')

## check amount of error
if len(errors) == 0 :
    print('OK')
else :
    # for loop -> print errors each line
    for i in range(len(errors)) :
        print(errors[i])
