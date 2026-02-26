# define 4 fns

def rotate_left(s,n) :
    # input s,n : s = string 0-9 , n is integer (0 < n < len(s))
    # return string which rotate left n pos.
    # Ex : rotate_left('12345' , 1) -> return '23451'
    # Ex : rotate_left('01234' , 3) -> return '34012'
    
    return s[n::1] + s[0:n:1] #cut at pos n -> right then left

def rotate_right(s,n) :
    # input s,n : s = string 0-9 , n is integer (0 < n < len(s))
    # return string which rotate right n pos.
    # Ex : rotate_right('12345' , 1) -> return '51234'
    # Ex : rotate_right('0123456' , 3) -> return '4560123'
    
    return s[-n::1] + s[0:-n:] # cut at pos -n -> right then left
def str_mod(s,n) :
    # input s,n : s = string 0-9 , n is integer (1 <= n <= 9)
    # return string which has len(s) which pos i return s[i] % n
    # Ex : str_mod('12345' , 5) -> return '12340'
    # Ex : str_mod('01234' , 5) -> return '01234'
    # Ex : str_mod('2468' , 2) -> return '0000'
    
    modded_str = ''
    for i in range(len(s)) : # for loop -> add str
        modded_str += str( int(s[i]) % n )
    return modded_str.strip()
        
def main() :
    # input : str s (0-9 at least 2 digits)
    # check second last digit conditions = m
    # if m = 1 -> rotate left
    # if m = 2 -> rotate right
    # if m = 3 -> str_mod
    # else -> show str s
    
    s = str(input().strip())
    last_digit = int(s[-1]) # int
    # check case
    if s[-2] == '1' : print(rotate_left(s,last_digit))
    elif s[-2] == '2' : print(rotate_right(s,last_digit))
    elif s[-2] == '3' : print(str_mod(s,last_digit))
    # else -> return s
    else : print(s.strip())
    
# execute input
exec(input().strip())