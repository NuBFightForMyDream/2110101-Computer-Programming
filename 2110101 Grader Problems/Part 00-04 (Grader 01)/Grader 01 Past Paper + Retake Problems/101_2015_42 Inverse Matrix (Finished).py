# 1 : รับ input ติดกัน (สมมติลองไม่ใช้ list comprehension) -> ลองใช้ for loop
list_mt = input('Enter A,B,C,D : ').split() #list(of str)
for i in range(4) : # ทำ 3 รอบ (0,1,2,3)
    list_mt[i] = float(list_mt[i]) # list (of float)
    
# 2 : เเทนตัวเเปรทีละตำเเหน่ง (จริงๆจะครอบ float(list)) เลยก็ได้ เเต่อยากฝึก for loop)
a = list_mt[0] ; b = list_mt[1] ; c = list_mt[2] ; d = list_mt[3] # float

# 3 : หา 1/det & ก้อนด้านใน
det = (a*d) - (b*c) # float

# กำหนด cd -> det ไม่เป็น 0 จะหา inv ได้
if det != 0 :
    
    # 3.1 : สลับตำเเหน่งก่อน
    a,d = d,a ; b *= -1 ; c *= -1  # ให้ ตป.หน้า มีค่าเป็น ค่าหลัง
        # (d มีปัญหา ต้องสลับค่ากันเองก่อน เเล้วค่อย x-1)
    
    # 3.2 : for loop (range วนใน list) เพื่อเปลี่ยนค่าเป็น inv
    for i in range(len(list_mt)) :
        list_mt[i] = (1/det) * list_mt[i]
    
    # เเทนเเต่ละตป.ใน list inv (a b c d -> d -b -c a)
    a_inv = str(list_mt[3]);  b_inv = str(-1 * list_mt[1]); c_inv = str(-1 * list_mt[2]); d_inv = str(list_mt[0])

    # print ทีละค่าออกมา
    print('Inverse of Matrix : ' , a_inv,b_inv,c_inv,d_inv)

# 3.2: det เป็น 0
elif det == 0 :
    print('Inverse of Matrix : ' , det)