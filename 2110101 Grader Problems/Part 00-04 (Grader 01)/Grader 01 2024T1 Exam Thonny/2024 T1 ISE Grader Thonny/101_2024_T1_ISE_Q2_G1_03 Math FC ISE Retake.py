# 1 : input list of int X
X = [float(e) for e in input().split()]

# 2 : define value
A = -1 ; B = 1 ; C = (A+B)/2 ; n = len(X) ; D = 0

# for loop #1 -> sum d
for i in range(n) :
    D += X[i] / (1+C)**i

# check condition
while abs(D) > 1e-8 :
    
    # check d pos/neg
    if D > 0 :
        A = C
    else :
        if D < 0 :
            B = C
        else : # D = 0
            pass
    # do this condition below
    C = (A + B) / 2
    D = 0
    i = 0
    
    # for loop n round
    for i in range(n) :
        D += ( X[i] / (1+C)**i )
        i += 1
        
else :
    print( round(C,8) )