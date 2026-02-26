# 1 : รับ input => บังคับ บรรทัดเเรก รับ input บนบรรทัดเดียวกัน
n,a,b = [int(e) for e in input('Enter N,A,B : ').split()]

# 2 : check cd a > b
if a > b :
    # do right
    d,e = -1 , -1
    # while loop
    while n < a :
        c = int(input())
        # check c > d
        if c > d :
            d , e = c , d # d = c , e = d
        else :
            if c > e :
                e = c
        n = n + b # เพิ่ม loop
    # print นอก loop while    
    print(d,e)
else :
    # do left -> เค้ากำหนดว่ารับ c,d,e,f เเยกบรรทัด
    c = int(input('Enter C : '))
    d = int(input('Enter D : '))
    e = int(input('Enter E : '))
    f = int(input('Enter F : '))
    
    # check if
    if e < f :
        e,f = f,e  # สลับค่า e,f
    # Y/N -> บังคับ check if
    if d < e :
        d,e = e,d # สลับ d,e
    if c < d :
        c,d = d,c
        
    if d > e :
        # Yes -> check d > f
        if d > f :
            # ไม่ต้องสลับค่า
            print(d,e) # print safe ทุกกรณี
        else :
            d,f = f,d # สลับ d,f
            print(d,e) # print safe ทุกกรณี
    else :
        if e > f :
            d,e = e,d # สลับ d,ำ
            print(d,e) # print safe ทุกกรณี
        else :
            d,f = f,d # สลับ d,f
            print(d,e) # print safe ทุกกรณี