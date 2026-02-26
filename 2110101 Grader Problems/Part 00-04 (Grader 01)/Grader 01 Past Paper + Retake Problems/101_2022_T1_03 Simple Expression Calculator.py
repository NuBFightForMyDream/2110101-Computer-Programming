## ข้อ 3 : (M) -> Simple Expression

# Key : รับทุกอย่างเข้ามาเป็น str -> check for loop วนตัวอักษร
expression = input('Enter Expression : ') #str

## เจอเเต่กรณี + , -

# for loop (range) -> check str
## Key : ถ้าเจอ +,- ==> เพิ่มช่ิงว่าง เพื่อเดี๋ยวจะ split ทีหลัง

# สร้าง str ใหม่ -> append str ที่เว้น spacebar เเล้ว
new_exp = ''
for c in expression :
    if c == '+' : 
        new_exp += ' +' # => เพิ่ม spacebar ด้านหน้า ให้เหมือนเเยกตัวเลข
        
    elif c == '-' :
        new_exp += ' -' # => เพิ่ม spacebar ด้านหน้า ให้เหมือนเเยกตัวเลข
    
    else :
        new_exp += c # ถ้าไม่ใช่ +, - ==> เพิ่ม str เดิม

## ลองเอามา split -> ใส่ลง list
list_num = new_exp.split() # เเยกช่องว่าง

sum = 0
for i in range(len(list_num)) : # วนทุกสมาชิกใน list_num (list of str)
    sum += int(list_num[i]) # เเปลงตัวที่ i เป็น int เเล้วบวกเข้าใน sum
    
print(sum) # ผลรวมทั้งหมด
