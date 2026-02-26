# ข้อ 1 : Flowchart 15 pts

# 1 : รับค่า a,b,c,d
a,b,c,d = [int(e) for e in input('Enter A,B,C,D : ').split()] #int,int,int,int

# 2 : check a>b ?
if a > b :
    # Yes : ทำฝั่งซ้าย
    a,b = b,a #สลับค่า a,b
    
    while d >= a :
        if c > d :
            a += 1
        else :
            d -= 1
    # ออก loop เเล้ว
    print(a,b,c,d)
    
# No : ฝั่งขวา
else :
    if c % 2 == 0 : # เช็คต่อว่าเป็นเลขคู่?
        d = d + a
    else :
        if d > c :
            c = c + d
        else :
            b = b + a
        # บังคับให้ a = b+c
        a = (b + c)
    # บังคับ print a,b,c,d
    print(a,b,c,d)
