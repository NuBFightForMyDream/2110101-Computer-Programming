# 1 : input info
num , loop = input().split()
num = float(num) ; loop = int(loop)

# 2 : for loop -> check if ses != 0
frac = []

# case 1 : first num isnt integer
if (num % 1) != 0 :
    # for loop with #loop
    for i in range(loop) :
        # divide num
        integer = num // 1
        # append str of int 
        frac.append( str(int(integer)) )
        
        # check if remainder < 1e-10 -> break
        if (num % 1) < 1e-10 :
            break
        else :
            # reverse ses/suan (change in ses)
            num = 1 / (num % 1)
        
    # out of loop -> print & join
    print(', '.join(frac))
    
# case 2 : first num is integer
else : # num is integer (divided by 1)
    print( int(num) )