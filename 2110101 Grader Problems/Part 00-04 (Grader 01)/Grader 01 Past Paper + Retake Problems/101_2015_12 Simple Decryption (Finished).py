# Key : check str ว่ากรอกเข้ามา 64 หรือ 128 ตัว
# ==> Fix ตน.ที่โจทย์บอก ให้เป็นตัวเลข ที่เหลือเป็นอะไรก็ได้

# 64 หลัก : บังคับลำดับที่ 8 22 34 49 เป็นตัวเลข
# 128 หลัก : บังคับลำดับที่ 3 12 24 32 56 89 92 101 เป็นตัวเลข

# 1 : รับ input (str) -> split (list of str)
passcode = input('Enter String (64 or 128 char) : ') # str -> อย่าลืม เรา index str ได้

# 2 : สร้าง list_num เพื่อเช็คว่าอยู่ใน หลักนั้นๆ อยู่ในเงื่อนไขของโจทย์มั้ย?
num = ['0','1','2','3','4','5','6','7','8','9'] #list(of str)

# 3 : สร้าง cd เช็ค ตน. (bool) => ถ้าไม่เข้า cd : print ว่าหารหัสไม่เจอ , ถ้าเข้า ให้ทำต่อ
cd64 = (passcode[7] in num) and (passcode[21] in num) and (passcode[33] in num) and (passcode[48] in num) #bool

cd128 = (passcode[2] in num) and (passcode[11] in num) and (passcode[23] in num) and (passcode[31] in num) \
        and (passcode[55] in num) and (passcode[88] in num) and (passcode[91] in num) and (passcode[100] in num) #bool

# 4 : สร้าง if ซ้อน if-elif เช็ค 64,128 ตัวอักษร

if len(passcode) == 64 : # Case 1 : 64 ตัว
    if cd64 == True :
        
        # 4.1 : กำหนด str ว่าง เพื่อค่อยๆบวกค่าเข้าไป (อย่าพึ่งใช้appendในlist)
        pin64 = '' #str
        
        # 4.2 : จากโจทย์ -> + str เข้าไปเรื่อยๆรอบเดียวพอ
        pin64 += passcode[7]  #pos8 (str)
        pin64 += passcode[21] #pos22 (str)
        pin64 += passcode[48] #pos49 (str) ## ระวัง ! โจทย์ให้ต่อ 49 ก่อน 34
        pin64 += passcode[33] #pos34 (str)
        
        # 4.3 : print ค่า pin64
        print('64-Digits PIN : ' , pin64) #str
                
    elif cd64 == False :
        print('Can\'t Find PIN , Try Again')
        
    
elif len(passcode) == 128 : # Case 2 : 128 ตัว
    if cd128 == True :
        
        # 5.1 : กำหนด str ว่าง (เเยก2ตัว เพราะเดี๋ยวเเปลงเป็น int เพื่อบวกกัน)
        pin128_1 = '' ; pin128_2 = ''
        
        # 5.2 : จากโจทย์ -> บวก str เเยกก้อน เเล้วนำมารวมกัน
        
        pin128_1 += passcode[2] #pos3 (str)
        pin128_1 += passcode[100] #pos101 (str)
        pin128_1 += passcode[23] #pos24 (str)
        pin128_1 += passcode[31] #pos32 (str)
        
        pin128_2 += passcode[55] #pos56 (str)
        pin128_2 += passcode[88] #pos89 (str)
        pin128_2 += passcode[91] #pos92 (str)
        pin128_2 += passcode[11] #pos12 (str)
        
        # 5.3 : เเปลงเป็น int -> รวมกัน /2 ปัดเศษ
        pin128 = (int(pin128_1) + int(pin128_2)) // 2 # int
        
        # 5.4 : print ค่า pin128
        print('128-Digits PIN : ' , str(pin128) ) # int -> str
        
    elif cd128 == False :
         print('Can\'t Find PIN , Try Again')

# 6 : in case ไม่ใช่ 64 หรือ 128 หลัก -> print หาไม่เจอ
else :
    print('Can\'t Find PIN , Try Again')


## Testcase : กำหนดมาให้

## 64 หลัก : LSKJJTS4R0EGZV4E1NDGR4JDAB03AFX3U06R2UJSYJY5OXO674E5HWRRTXZRR766 => 4470
## 64 หลัก : 3ZCCGNO8R6CXTOPOQADTI7Z947D7B9LZ58BLPNJ3Y154BGPY01DGBF93DROU6FHC => 8708

## 128 หลัก : vv3LldHypWS2Fxk9wHdmVJo5aytuJhf5m6ZrFVPvjIFPfPzbOGPGDwE6F1B7xGG
           # 8QwqP3q0zAEVyv3U9jYyVjcpl2Hj30BQgB99U7N0vKntSIwTaYVnJeDbu9C9JBOCb => 4993 (1 : 3755, 2 : 6232)

## 128 หลัก : rv4mecdgqeu0zulhmhhhduy6tfwvbtp8tkmbpanxjatzwppayvaqeep0muvbjhb
           # dilhufkznuygmzkwdcjbqcmgi0ol3zxqzduvp9txxqkoshvsjthowiudqpjosobyr => 2499 (1 : 4968, 2 : 0030)
           