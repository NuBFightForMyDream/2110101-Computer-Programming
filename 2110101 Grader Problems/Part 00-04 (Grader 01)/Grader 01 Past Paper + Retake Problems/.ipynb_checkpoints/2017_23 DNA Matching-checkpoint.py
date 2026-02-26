# 1 : รับ str DNA 1 , DNA 2 เข้ามาก่อน + ตั้ง ตป. check
dna1 = str(input('Enter DNA 1 : ')) #str
dna2 = str(input('Enter DNA 2 : ')) #str
check = True # ตั้งให้เป็น True ก่อน

# 2 : for loop
for i in range(len(dna1)) :
    
    if (dna1[i] == 'A' and dna2[i] == 'T') :
        pass

    elif (dna1[i] == 'T' and dna2[i] == 'A') :
        pass

    elif (dna1[i] == 'G' and dna2[i] == 'C') :
        pass

    elif (dna1[i] == 'C' and dna2[i] == 'G') :
        pass
    
    else :
        print('False')
        check = False # เปลี่ยนให้ check เป็น False
        break
    
# 3 : check ว่าถ้า True -> ให้ print True
if check == True :
    print('True')
