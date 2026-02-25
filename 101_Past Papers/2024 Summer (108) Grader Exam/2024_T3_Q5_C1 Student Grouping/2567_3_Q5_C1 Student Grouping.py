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
    for [stu_id , course_number] in info_student :
        
        if str(stu_id)[0:2] == '65' :
            id65_student.append( stu_id )
            
        elif str(stu_id) [0:2] == '66' :
            id66_student.append( stu_id )
            
        elif str(stu_id) [0:2] == '67' :
            id67_student.append( stu_id )
            
    # sort list (no need to do in this problem)
    # id65_student = sorted(id65_student) ; id66_student = sorted(id66_student) ; id67_student = sorted(id67_student)
        
    # print list (joint list of int by *)
    print(*id65_student) ; print(*id66_student) ; print(*id67_student) ; 
    
if type_of_grouping == 2 : # sort nisit by faculty (engineering , medical)
    
    # create list for 65,66.67 students
    engineering_student = [] ; medical_student = []
    
    # check then store
    for [stu_id , course_number] in info_student :
        
        if str(stu_id)[-2:] == '21' : # engineering student
            engineering_student.append( stu_id )
            
        elif str(stu_id)[-2:] == '30' : # medical student
            medical_student.append( stu_id )
            
    # sort list by id (no need to do in this problem)
    # engineering_student = sorted(engineering_student) ; medical_student = sorted(medical_student)
        
    # check which faculty is longer (the one longer , print it first)
    if len(medical_student) > len(engineering_student) :
        print(*medical_student) ; print(*engineering_student)
    else :
        print(*engineering_student) ; print(*medical_student)
        
elif type_of_grouping == 3 : # sort nisit by course_number (!! this problem has >2 subj , so using dict is better)
    
    # create dict for storing student
    info_course = {} # key = course_number , value = list of nisit's id
    
    # for loop each stu_id and store
    for [stu_id , course_number] in info_student :
        
        # check if course_number exist
        if course_number not in info_course :
            info_course[ course_number ] = [stu_id] # create new list
        else :
            info_course[ course_number ] += [stu_id] # append new stu_id
            
    # for loop each course_number then print value (list of nisit's id)
    for course_number in info_course :
        print(*info_course[course_number]) # join list
    