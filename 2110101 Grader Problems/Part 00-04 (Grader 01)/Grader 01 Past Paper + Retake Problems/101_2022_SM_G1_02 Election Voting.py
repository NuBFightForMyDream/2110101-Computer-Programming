# 2022 Summer : Grader 1 02 Election
# 50 min ==> ช้าสัส!!! เดะปรับปรุงโค้ดเพิ่มให้กระชับลง

## logic : เลือกผู้สมัคร & เลือกพรรค เเยกกัน -> เอา max ของเเต่ละอย่าง เเสดงออกมา

# 1 : สร้าง list ที่จำเป็นต้องใช้
SNames = ["A1", "B2", "C3", "D4", "E5", "F6", "G7", "H8", "X9", "Y10", "Z11"]
PNames = ["PT1", "PP2", "RT3", "TT4", "KK5", "ST6"]

point_people = []   # append คะเเนนของคน ที่รับเข้ามา
point_party = []  # append คะเเนนของพรรค ที่รับเข้ามา

# 2 : input info เข้ามา (เดี๋ยวค่อย split ทีหลัง)
info = input('Enter Number & Party : ')

# 3 : while loop -> ตราบใดรับมาเเล้วยังไม่เป็น q
while info != 'q' :
    
    # 3.1 : split & index ของเเต่ละคน
    people = (info.split())[0] #str(int)
    party = (info.split())[1] #str(int) 
    
    # 3.2 : append ค่าเข้า list people, party   
    point_people.append(int(people)) # append int
    point_party.append(int(party)) # append int
    
    # 3.3 : รับ input ตอนสุดท้าย
    info = input('Enter Number & Party : ')
    
# 3 : สร้าง count_people , count_party เป็น list 0 ก่อน -> append ค่าทีหลัง
count_people = [0] * len(SNames) # ขนาด = จน.ผู้สมัคร (11
count_party = [0] * len(PNames) # ขนาด = จน.พรรค (6)

## ตอนนี้ มี list point_name , point_party เก็บคะเเนน (ไม่เรียงคน/พรรค เรียงตามที่ป้อนเข้ามา)
## ตอนนี้ มี list count_name , count_party เก็บจน.ผลโหวต (เป็น list 0)

## 4 : for loop ซ้อน for loop => ถ้าเจอเลขคน ให้ break loop ใน (loop นอกวนครบจน.คน)

# 4.1 : วน for loop ของ people
for i in range(len(point_people)) :
    check_people = point_people[i]
    
    for j in range(1,12) : # วน 11 รอบ => เริ่มคนที่ 1 เพราะสามารถ index 0 ได้ & กันตัวท้าย error
        if check_people == j :
            count_people[j-1] += 1
            break

# 4.2 : วน for loop ของ party 
for i in range(len(point_party)) : 
    check_party = point_party[i]
    
    for j in range(1,7) : # วน 6 รอบ => เริ่มคนที่ 1 เพราะสามารถ index 0 ได้ & กันตัวท้าย error
        if check_party == j :
            count_party[j-1] += 1
            break
        
# 5 : ตอนนี้ได้ list count ของทั้งคู่เเล้ว -> หา max เพื่อ index ตัว
max_people = max(count_people)
max_party  = max(count_party)

idS = count_people.index(max_people)
idP = count_party.index(max_party)

print( SNames[idS] , max_people ) # print ชื่อผู้ชนะ & คะเเนนโหวตมากสุด
print( PNames[idP] , max_party ) # print ชื่อผู้ชนะ & คะเเนนโหวตมากสุด
