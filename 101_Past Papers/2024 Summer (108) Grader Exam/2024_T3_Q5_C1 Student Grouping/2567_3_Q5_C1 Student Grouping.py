#
# 2567_3_Q5_C1: Student Grouping 
#

# 1 ; input filename
fn, type_of_grouping = input().split()
type_of_grouping = int(type_of_grouping)

filename = open(fn , 'r')

# store info for grouping
info_student = []

filename = open(fn ,'r')
    
for line in filename : 
    # store info into info_student (list of list)
    stu_id , course_number = line.split()[0] , line.split()[1]
    info_student.append( [stu_id , course_number] )
    
# check type of grouping
if type_of_grouping == 1 : # sort nisit by stu_id (65 , 66 , 67)
    # create list for 65,66.67 students
    id65_student = [] ; id66_student = [] ; id67_student = []
    # check then store
    for [stu_id , course_name] in info_student :
        
        if str(stu_id)[0:2] == '65' :
            id65_student.append( stu_id )
            
        elif str(stu_id) [0:2] == '66' :
            id66_student.append( stu_id )
            
        elif str(stu_id) [0:2] == '67' :
            id67_student.append( stu_id )
            
    # sort list
    # id65_student = sorted(id65_student) ; id66_student = sorted(id66_student) ; id67_student = sorted(id67_student)
        
    # print list
    print(*id65_student) ; print(*id66_student) ; print(*id67_student) ; 
    
elif type_of_grouping == 2 : # sort nisit by stu_id (65 , 66 , 67)
    # create list for 65,66.67 students
    engineering_student = [] ; medical_student = []
    # check then store
    for [stu_id , course_name] in info_student :
        
        if str(stu_id)[-2:] == '21' :
            engineering_student.append( stu_id )
            
        elif str(stu_id)[-2:] == '30' :
            medical_student.append( stu_id )
            
    # sort list
    # engineering_student = sorted(engineering_student) ; medical_student = sorted(medical_student)
        
    # print list
    if len(medical_student) > len(engineering_student) :
        print(*medical_student) ; print(*engineering_student)
    else :
        print(*engineering_student) ; print(*medical_student)
        
elif type_of_grouping == 3 : # sort nisit by stu_id (65 , 66 , 67)
    # create list for 65,66.67 students
    compprog_student = [] ; othersubj_student = []
    # check then store
    for [stu_id , course_name] in info_student :
        
        if course_name == '2110101' :
            compprog_student.append( stu_id )
            
        elif course_name != '2110101' :
            othersubj_student.append( stu_id )
            
    # sort list
    # engineering_student = sorted(engineering_student) ; medical_student = sorted(medical_student)
        
    # print list
    print(*compprog_student) ; print(*othersubj_student)
    
filename.close()