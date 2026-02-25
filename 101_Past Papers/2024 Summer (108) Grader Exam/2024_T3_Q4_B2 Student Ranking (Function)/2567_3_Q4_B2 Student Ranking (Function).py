#
# 2567_3_Q4_B2: Student Ranking (Function) 
#

import math

def calculate_average(scores):
    return sum(scores) / len(scores)

def get_grade(average_score):
    if average_score >= 80 : return 'A'
    elif 75 <= average_score < 80 : return 'B+'
    elif 70 <= average_score < 75 : return 'B'
    elif 65 <= average_score < 70 : return 'C+'
    elif 60 <= average_score < 65 : return 'C'
    elif 55 <= average_score < 60 : return 'D+'
    elif 50 <= average_score < 55 : return 'D'
    else : return 'F'
    
def process_student_data(stu_data):
    # stu_data = [ stu_name , list_of_score ]
    
    ## define var first
    stu_name = stu_data[0] ; list_of_score = stu_data[1] ;
    letter_grade = get_grade( calculate_average ( list_of_score ) )
    
    # return result (list)
    return [ stu_name , letter_grade ]

def print_students_ranked_by_grades(list_of_stu_data):
    
    # define list of all grades
    grade_A = [] ; grade_B_plus = [] ; grade_B = [] ; grade_C_plus = []
    grade_C = [] ; grade_D_plus = [] ; grade_D = [] ; grade_F = []
    
    # store info into info_student
    for [stu_name , list_of_score] in list_of_stu_data :
        
        # Note : process..() will get [stu_name , letter_grade] -> index 1 is letter_grade
        if process_student_data( [stu_name , list_of_score] )[1] == 'A' :
            grade_A.append(stu_name)
        
        elif process_student_data( [stu_name , list_of_score] )[1] == 'B+' :
            grade_B_plus.append(stu_name)
        
        elif process_student_data( [stu_name , list_of_score] )[1] == 'B' :
            grade_B.append(stu_name)
        
        elif process_student_data( [stu_name , list_of_score] )[1] == 'C+' :
            grade_C_plus.append(stu_name)
            
        elif process_student_data( [stu_name , list_of_score] )[1] == 'C' :
            grade_C.append(stu_name)

        elif process_student_data( [stu_name , list_of_score] )[1] == 'D+' :
            grade_D_plus.append(stu_name)
        
        elif process_student_data( [stu_name , list_of_score] )[1] == 'D' :
            grade_D.append(stu_name)
            
        elif process_student_data( [stu_name , list_of_score] )[1] == 'F' :
            grade_F.append(stu_name)
    
    # sort each list then print
    grade_A = sorted(grade_A) ; grade_B_plus = sorted(grade_B_plus) ; grade_B = sorted(grade_B)
    grade_C_plus = sorted(grade_C_plus) ; grade_C = sorted(grade_C) ; grade_D_plus = sorted(grade_D_plus)
    grade_D = sorted(grade_D) ; grade_F = sorted(grade_F)
    
    # for loop print
    for stu_name in grade_A : print( stu_name , 'A' )
    for stu_name in grade_B_plus : print( stu_name , 'B+' )
    for stu_name in grade_B : print( stu_name , 'B' )
    for stu_name in grade_C_plus : print( stu_name , 'C+' )
    for stu_name in grade_C : print( stu_name , 'C' )
    for stu_name in grade_D_plus : print( stu_name , 'D+' )
    for stu_name in grade_D : print( stu_name , 'D' )
    for stu_name in grade_F : print( stu_name , 'F' )
    
# DO NOT REMOVE or MODIFY THE NEXT 3 LINES
while (cmd:=input().strip()):
    exec(cmd)
    if cmd[-1]==';': break