#
# 2567_3_Q3_A1: 2567_3_Q3_A1: Flowchart 
#

# input info
a,b,c,d,e = [int(e) for e in input().split()]

if a > 0 :
    if a % 2 == 0 :
        if b < c :
            b *= e
        else :
            if b < d :
                b //= e
            b -= e
    else :
        if b > c :
            b,c = c,b
        if b > d :
            b,d = d,b
        else :
            b += e
    
else :
    while not (a > d) :
        a += 1
        if a > b :
            break
        else :
            b -= 1

print(a,b,c,d,e)