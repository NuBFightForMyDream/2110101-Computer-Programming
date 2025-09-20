# 1 : define grade letter list
grade_letter = ['A','B+','B','C+','C','D+','D','W','F']
sum_credit = 0
sum_point = 0 # gpa x credit

# 2 : input info
for i in range( int(input()) ) : 
    codename , credit , grade = input().split()
    
    # index grade in list
    if grade != 'W' : # calculate if not withdraw
        
        sum_credit += int(credit) # add credit if not withdrawed
        
        grade_point = 4 - (grade_letter.index(grade)) / 2
        
        # sum point
        sum_point += grade_point * int(credit)

# 3 : print format
gpax = sum_point / sum_credit
print( round(gpax , 2) )