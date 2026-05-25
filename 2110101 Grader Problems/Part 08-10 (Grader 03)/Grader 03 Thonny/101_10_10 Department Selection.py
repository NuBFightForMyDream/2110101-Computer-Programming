# define space
result = [] # format -> "6730084521" : "EE"
seats_available = {} # format -> "CP" : 20

dept_count = int(input())
for i in range(dept_count) :
    dept , seat = input().strip().split()
    # create key:val
    seats_available[dept] = int(seat) 


## store info then sort by department
ranked_student_info_by_score = []

students_count = int(input())
for i in range(students_count) :
    student_id , score , rank1 , rank2 , rank3 , rank4 = input().strip().split()
    
    # store info
    ranked_student_info_by_score.append([-float(score) , student_id , rank1 , rank2 , rank3 , rank4])
    
# after stored , sort info by score
ranked_student_info_by_score.sort()

## seating algorithm
for each_student in ranked_student_info_by_score :
    # each_student = [-int(score) , student_id , rank1 , rank2 , rank3 , rank4]
    student_id , rank1 , rank2 , rank3 , rank4 = each_student[1:]
    
    ## check if each dept is full
    if seats_available[rank1] > 0 :
        result.append([student_id , rank1])
        # decrease seat by 1
        seats_available[rank1] -= 1
        
    elif seats_available[rank2] > 0 :
        result.append([student_id , rank2])
        # decrease seat by 1
        seats_available[rank2] -= 1
        
    elif seats_available[rank3] > 0 :
        result.append([student_id , rank3])
        # decrease seat by 1
        seats_available[rank3] -= 1
        
    elif seats_available[rank4] > 0 :
        result.append([student_id , rank4])
        # decrease seat by 1
        seats_available[rank4] -= 1
        
## sort result by student_id
result.sort()

for each_student in result :
    print(each_student[0] , each_student[1])
        
    