## Using Nested Dict & Nested Loop -> Challenging For Beginners

# 1 : input info
info_courses = dict() # nested dict

# 2 : for loop -> input info
for num in range( int(input()) ) :
    # split info into 2 parts
    info = input().split()
    ids = info[0] ; courses = info[1:]
    stu_yr = 2500 + int(ids[0:2]) # 25XX (int)
    
    # for loop each courses in info we've input
    for course_id in courses :
        
        # case 1 : course id not in dict -> add new key-val -> check stu
        if course_id not in info_courses :
            # 1.1 : create new key-val to dict
            info_courses[each_course] = dict() # subdict
            
            # 1.2 : check if student in course (key = yr , val = amount of stu)
            if stu_yr not in info_courses[each_course] :
                info_courses[each_course][stu_yr] = 1 # set new value to 1 
            else :
                info_courses[each_course][stu_yr] += 1 # add value +1
                
        # case 2 : course id in dict -> check stu
        else : # check if student in course (key = yr , val = amount of stu)
            if stu_yr not in info_courses[each_course] : 
                info_courses[each_course][stu_yr] = 1  # set new value to 1
            else :
                info_courses[each_course][stu_yr] += 1 # add value +1

# 3 : check input -> print str
check = input().split()
for ele in check : # each line
    
    # 3.1 : check if course in info_courses 
    if ele in info_courses :
        info_stu = info_courses[ele] # sublist we'll print
        info_stu = dict(sorted(years.items())) # sorted dict (with .items) -> change to dict
        # add to str (have pb with space in dict)
        str_out = ''
        for each_key in years :
            str_out += str(each_key) + ':' + str(years[each_key]) + ', '
        print(ele , str_out.strip(', ')) # strip out last ', '
    
    # 3.2 : course not in info_courses -> print None
    else :
        print(ele , 'None')