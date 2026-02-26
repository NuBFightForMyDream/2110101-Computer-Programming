# Logic : check Royal ก่อน ค่อยเช็คย่อยลงไป
n = int(input('Enter Loop : ')) #  รับ input จน. loop

# สร้าง list of str ของเลขไพ่ เพื่อเช็ค order
num = ['A','2','3','4','5','6','7','8','9','X','J','Q','K']

for i in range(n) : # วน loop ตาม จน.ที่รับเข้ามา
    
    # 1 : str -> ตัดข้าง (Strip) -> split => index เป็น str
    inp = input("Enter 5 Cards Info : ").strip() # strip ตัวว่างข้างๆ ก่อน
    d1,d2,d3,d4,d5 = (inp.strip('|')).split('|') # strip | ตัวข้าง -> split ด้วย |
    
    # 2 : เเอบใช้ index เพื่อหา ตน.ใน list -> เอาตัวเลข (index 0)
    id1 = num.index(d1[0]) ; id2 = num.index(d2[0]) ;  id3 = num.index(d3[0]) ; 
    id4 = num.index(d4[0]) ; id5 = num.index(d5[0])
    
    # 3 : สร้างcd เช็ค T/F
        # 3.1 : checkเลขที่เรียง -> ห่างกัน -1 เสมอ เลย fix ให้ตัวสุดท้ายมีค่า id5 -> เทียบให้ตัวอื่นเท่ากัน
    sortnum = ( (id1-4) == (id2-3) == (id3-2) == (id4-1) == id5)
        # 3.2 : เจอเคสว่า A สามารถอยู่ได้ 2 ที่ -> 1 or max (สูงกว่า K) -> บังคับเรียง AKQJX
    sortnum_ace = (d1[0] == 'A' and d2[0] == 'K' and d3[0] == 'Q' and d4[0] == 'J')
        # 3.3 : หน้าเดียวกันมั้ย -> check ที่ index 1 ของเเต่ละตัว
    sameface = (d1[1] == d2[1] == d3[1] == d4[1] == d5[1])
        # 3.4 : cd พิเศษ -> เป็น sortnum (ที่เรียง AKQJX) เเละ หน้าเหมือน
    royal = (sortnum_ace) and (sameface)
    
    # 4 :  ไล่เช็คทีละ cd -> เช็คให้ครอบคลุม => print เลย (โจทย์ต้องการ)
        # 4.1 : cd พิเศษ -> royal -> Royal Straight Flush
    if royal :
        print('Royal Straight Flush')
        
        # 4.2 : เลขเรียง (ไม่จำเป็นต้อง AKQJX) 
    elif sortnum and sameface :
        print('Straight Flush')
    
        # 4.3 : กรณี เลขเรียง หน้าไม่ตรง (เช็คเลขเรียง2 เเบบบ ใช้ or เพราะเช็คทั้งคู่ เลือก 1 ใน 2)
    elif (sortnum and (not sameface)) or (sortnum_ace and (not sameface)) :
        print('Straight')
        
        # 4.4 : หน้าตรง only -> นับเป็น Flush (เช็คเเบบ4.3)
    elif (not sortnum) and (sameface) or (not sortnum_ace and sameface) :
        print('Flush')
        
        # 4.5 : ไม่ตรงcase ไหน => ให้เป็น None
    else :
        print('None')
        
        