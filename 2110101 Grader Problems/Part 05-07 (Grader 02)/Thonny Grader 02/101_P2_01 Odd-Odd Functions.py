# 1 : check if number is odd -> return T/F
def is_odd(n) :
    if n % 2 == 0 :
        return False
    elif n % 2 != 0 :
        return True 
    
# fn 2 : 
def has_odds(x) :
    # give first status = False
    check_odd = False
    # for loop -> check if found odd nb. -> if found = break
    for i in range(len(x)) :
        if x[i] % 2 != 0 :
            check_odd = True
            break # out of loop
    # return T/F
    return check_odd

# fn 3 : check all member odd -> return T/F
def all_odds(x) :
    check_allodd = True
    # for loop -> check each ele.
    for i in range(len(x)) :
        if x[i] % 2 == 0 :
            check_allodd = False
            break
    # out of loop -> return T/F
    return check_allodd

# fn 4 : check all member are even (no odd) -> return T/F
def no_odds(x) :
    check_noodd = True
    # for loop -> if found odd -> return False
    for i in range(len(x)) :
        if x[i] % 2 != 0 :
            check_noodd = False
    # out of loop -> return T/F
    return check_noodd

# fn 5 : receive only odd numbers
def get_odds(x) : # parameter x = list
    
    
    