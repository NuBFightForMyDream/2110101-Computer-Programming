## solution 1 : add all info then filter 

# default data
student_info = [] # for storing all data 
groups = ['A','B','C','Dog','E','F','G','H','J','K','L','M','N','P','Q','R','S','T']
departments = ['General','CE','EE','ME','AE','IE','CE','GE','PE','ENV','SV','MT','CP','CEDT','NT','ADME','AERO','SEMI','ICE','AI','NANO']
intania_gens = list(map(str, range(80, 121)))

# input 
N = int(input())
for i in range(N) : 
    name , group , gen , dept = input().strip().split()
    gen = int(gen) 
    
    # add info to student_info
    student_info.append( [name , group , gen , dept] )
    
filter_in = input().split()

## checking algorithm 

for check in filter_in : 
    ## refresh vopied filter list every time
    filtered = []
    
    ## case 1 : in group
    if check in groups : 
        for each_student in student_info : 
            if each_student[1] == check : 
                filtered.append(each_student)
                
    # case 2 : in department 
    elif check in departments : 
        for each_student in student_info : 
            if each_student[3] == check : 
                filtered.append(each_student)
                
    ## case 3 : in intania_gen
    elif check in intania_gens : 
        for each_student in student_info : 
            if each_student[2] == int(check) : 
                filtered.append(each_student)
        
    ## replace old data with filtered data 
    student_info = filtered 
    
## after filtered , print each data 
student_info.sort()
for each_student in student_info : 
    print(each_student[0] , each_student[1] , each_student[2] , each_student[3])