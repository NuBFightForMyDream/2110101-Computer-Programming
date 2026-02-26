# 1 : input a,b,c,d
a,b,c,d = [int(e) for e in input().split()]

# 2 : check condition
if a == 1 : 
    # sum a
    a = b + c + d
    # Yes -> Do Left
    if b == 1 : 
        c += (c+d)
    elif b == 2 :
        c += (c-d)
    else : 
        if b > 4 : 
            c += (c * d)
        # do b > 5 but not doing b == 1 if True
        if b > 5 : 
            c += (c % d)
        else : 
            c += (c // d)
            
    # print c
    print(c)
    
else : 
    while b < c : 
        b += 1
        if b > a : 
            break
        else :
            c -= 1 
        # if inside or outside else didnt affect cuz break before
        if a > d : 
            break 
        else :
            a += c
    
# print a,b,c,d
print(a,b,c,d) 