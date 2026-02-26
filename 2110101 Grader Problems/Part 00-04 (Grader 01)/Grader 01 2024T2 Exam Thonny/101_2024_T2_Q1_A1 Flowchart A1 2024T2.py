# input a,b,c
a,b,c = [int(e) for e in input().split()]

# check a < b ?
if a < b :
    d = c
    x = 'B' # binary digits
    
    if c == 0 :
        x = str(c) + x
        
    else :
        while c > 0 :
            r = c % 2
            # add string in front x to x
            x = str(r) + x
            # divide 2 (floor 2)
            c = c // 2
            
    # print d,x
    print(d,x)
    
else :
    # check a > b
    if a > b :
        # input d
        d = int(input())
        # check a > c
        if a > c :
            a,b = b,a
            a,c = c,a
            a += 1
            b = 2*b
        # must check b>d
        if b > d :
            b,d = d,b
            a += 2
            b = 3*b
        # add c , decrease b
        c = a + 2*b
        d = c - 3*a
        # print a,b,c,d
        print(a,b,c,d)
        
    else : # formula
        e = float(input())
        f = float(input())
        out = e * (1 + (f/(100*a)))**(a*c)
        print( round(out , 2) )
            
        