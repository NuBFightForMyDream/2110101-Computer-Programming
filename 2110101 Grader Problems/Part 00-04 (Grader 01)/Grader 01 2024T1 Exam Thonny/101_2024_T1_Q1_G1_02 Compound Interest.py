# 1 : input & split info
info = input().split() # dmy savings m_save m_start
bm = int(info[0].split('/')[1])
savings = float(info[1]) ; m_save = int(info[2])
m_start = int(info[3])

# 2 : for loop -> check logic
## general case (no birthdate)
# i = 0 -> rate = 1 , i = 1 -> rate = 2
# i = 2 -> rate = 3 , i = 3 -> rate = 4
# i = 4 -> rate = 1 --> rate = (i%4)+1

## check bm by i + m_start mod 12 == bm
## don't forget that month in range 1 to 12 -> -1 then mod 12 then + 1
for m in range(m_save) :
    
    # case 1 : same as birth month -> (now+m_start-1)mod 12 + 1
    if ( (m + m_start) - 1) % 12 + 1 == bm :
        savings += (1/12) * (m%4+1+1)/100 * (savings) # plus rate 0.01 (max rate can be 0.05)
       
    # case 2 : general case -> use formula
    else :
        savings += (1/12) * (m%4+1)/100 * (savings)
    
# 3 : print & round savings 2 dec. pts
print(round(savings , 2))