# สร้าง 5 fn โดยกำหนด a,b,c ดังนี้
# - a,b,c = int มีค่าตต. -1000 to 1000
# - มีอย่างน้อย 1 ค่า > 0
# - มีอย่างน้อย 1 ค่า < 0

def f1(a,b,c) :
    # คืน int ที่มีค่าน้อยสุดใน a,b,c -> คิดเฉพาะตัวมีค่า >0
    list_num = [a,b,c]
    if (a < 0) : list_num.remove(a)
    if (b < 0) : list_num.remove(b)
    if (c < 0) : list_num.remove(c)
    
    minimum = min(list_num)
    return minimum

def f2(a,b,c) :
    # คืน int ที่มีค่าน้อยสุดใน a,b,c -> คิดเฉพาะตัวมีค่า <0
    list_num = [a,b,c]
    if (a > 0) : list_num.remove(a)
    if (b > 0) : list_num.remove(b)
    if (c > 0) : list_num.remove(c)
    
    maximum = max(list_num)
    return maximum

def f3(a,b,c) :
    sum = a + b + c
    sum_str = str(abs(sum)) # ใส่ abs เผื่อค่าติดลบ
    firstdigit_int = int(sum_str[0]) 
    return firstdigit_int

def f4(a,b,c) :
    sum = a + b + c
    sum_str = str(abs(sum)) # ใส่ abs เผื่อค่าติดลบ
    lastdigit_int = int(sum_str[-1]) 
    return lastdigit_int

def main() :
    s1 , s2 , a , b , c = [int(e) for e in input().split()]
    
    if (s1 == 0) and (s2 == 0) :
        print(f1(a,b,c)) # call fn -> parameter เป็น a,b,c ที่รับเข้ามา
        
    elif (s1 == 0) and (s2 == 1) :
        print(f2(a,b,c)) # call fn -> parameter เป็น a,b,c ที่รับเข้ามา
        
    elif (s1 == 1) and (s2 == 0) :
        print(f3(a,b,c)) # call fn -> parameter เป็น a,b,c ที่รับเข้ามา
        
    elif (s1 == 1) and (s2 == 1) :
        print(f4(a,b,c)) # call fn -> parameter เป็น a,b,c ที่รับเข้ามา
        
    else :
        print('Error')
    
# check fn -> exec
exec(input().strip())
    