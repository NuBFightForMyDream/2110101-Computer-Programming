# Interest เดิม : 5% py (ฝากเกิน 12 เดือน)
# ถอนก่อน 1 ปี -> 0.75% py
# ฝาก 1-2 ปี -> ทบต้นเเล้วคิดดอกเบี้ย
# ฝาก 2-3 ปี -> ทบต้น 2 รอบ + คิดส่วนเกิน (ดอกเบี้ย 6.5% ต่อปี)

# 1 : input เงินต้น + จน.เดือน (list comprehension)
savings , month = [float(e) for e in input('Enter Savings , Month : ').split()] #float float
# savings = float , month = float

# 2 : สร้าง 4(+1) condition เก็บเงินฝาก

# cd 1 : ฝากไม่ถึง 12 เดือน => ดอกเบี้ย 0.75 % ต่อปี
if 0 <= month < 12 :
    interest = savings * (0.75/100) * (month/12)
    # หาร 100 เพื่อให้เป็นค่าจริง , คูณ month เพื่อคิดเป็น x% ต่อ จน.เดือน
    savings += interest
    
    interest_total = interest
    print('Total Savings : ' , savings)
    print('Total Interest : ' , interest_total)
    
# cd 2 : ฝากตต. 12 เดือน เเต่ไม่เกิน 24 เดือน => คิดทบต้น 1 รอบ เเล้วคิดดอกเบี้ย 5% ต่อปี
elif 12 <= month < 24 :
    interest_yr0 = savings * (5/100)
    savings += interest_yr0 #ทบต้นเเล้ว
    
    interest_yr1 = savings * (5/100) * ((month-12)/12)
    savings += interest_yr1 # ทบต้นรอบ 2
    
    interest_total = interest_yr0 + interest_yr1
    print('Total Savings : ' , savings)
    print('Total Interest : ' , interest_total)
    
# cd 3 : ฝากตต. 24 เดือน เเต่ไม่เกิน 32 เดือน => ทบต้น 2 รอบ เเล้วคิดส่วนเกิน
elif 24 <= month < 36 :
    interest_yr0 = savings * (5/100)
    savings += interest_yr0
    
    interest_yr1 = savings * (5/100)
    savings += interest_yr1
    
    interest_yr2 = savings * (6.5/100) * ((month-24)/12)
    savings += interest_yr2
    
    interest_total = interest_yr0 + interest_yr1 + interest_yr2
    print('Total Savings : ' , savings)
    print('Total Interest : ' , interest_total)
    
elif month >= 36 :
    print('Access Denied : >36 Month Savings')
    
# Note : มี 4 testcases => print total
# 1 : ฝาก 11 เดือน => 50000 11 => 50343.75
# 2 : ฝาก 17 เดือน => 75000 17 => 80390.625
# 3 : ฝาก 29 เดือน => 125000 29 => 141544.92
# 4 : ฝาก 37 เดือน => 12000 37 => Access Denied
