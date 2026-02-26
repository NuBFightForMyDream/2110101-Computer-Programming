# Key : ต้องการหาค่า arcsin(x) โดยคำนวณตามสูตร n = 0,1,2
# ให้ค่าเริ่มเต้น arcsin(x) เป็น 0

# 1 : รับค่า x เข้ามา + import math + define var.
import math
x = float(input('Enter X : ')) #float
arcsin = 0

# 2 : วน for loop ในเงื่อนไข abs(x) <= 1
if abs(x) <= 1 :
    for n in range(0,3,1) : # ทำ 3 รอบ (0,1,2)
        
        # 2.1 : define ses , suan
        ses = math.factorial(2*n) * (x**(2*n+1))
        suan = (4**n) * (math.factorial(n))**2 * (2*n+1)
        
        # 2.2 : บวกค่า arcsin เข้าไปใน ตป.เดิม
        arcsin += (ses / suan)
        
# 3 : print ค่าประมาณ Talor Approx. (ยิ่งประมาณเยอะยิ่งดี)
print('Taylor Approx. of arcsin(x) : ' , arcsin)