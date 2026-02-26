# 1 : input m,n & import math
import math
m,n = [int(e) for e in input().split()]

# 2 : check m,n
if m < n :
    # input a,b,c
    a,b,c = [int(e) for e in input().split()]
    # check odd/even m
    if m % 2 != 0 :
        # set u,v,w,k to 0
        u = 0 ; v = 0 ; w = 0 ; k = 0
        # while loop
        while m > k :
            # check  a > b :
            if a > b :
                if a + c >= k :
                    u += 3
                    v -= 2
                    w += 1
                else :
                    u -= 1
                    v += 2
                    w += 3
            else :
                b = (a+b) / 2
            # increment k by 1
            k += 1
        # out of while loop -> print u,v,w
        print(u,v,w)
    else :
        # swap a,b
        a,b = b,a
        # do math algorithms
        a = c - 2*b
        c = a**2
        b = 3*c + 1
        # print a,b,c
        print(a,b,c)
        
else : # m >= n
    if m == n :
        s = int(input())
        # given i,k = s
        i = s ; k = s
        
        # for loop
        for j in range(0 , m-1) :
            # input x
            x = int(input())
            if x < i :
                i = x
            if x > k :
                k = x
                
        # area of rectangle width i , height k
        area = i * k
        print(area)
        
    else :
        if (m + n) % 3 == 0 :
            r = m**(1/2) + n**(1/3)
        else :
            r = math.sin((m * math.pi) / (m+n)) + math.cos((n * math.pi) / (m+n))
        # print r but round 2 decimal pts
        print( round(r,2) )
   