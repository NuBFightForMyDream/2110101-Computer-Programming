# 1 : open file

nisit_female = []
nisit_male = []

filename = input() 
nisit_info = open(filename , 'r')
    
# read each line
for line in nisit_info :
    
    # no need to readline again
    stu_id , gender , fac , sec , lecturer = line.strip().split(',')
    
    # check gender
    if gender == 'F' :
        nisit_female += [ [sec , lecturer] ]
        
    elif gender == 'M' :
        nisit_male += [ [sec , lecturer] ]
        
# read already -> close file
nisit_info.close()

# 2 ; check lecturer
lecturer_in = input() # Enter Lecturer Name

# for loop female & male for check
    
if lecturer_in == 'AAA' :
    female_count = 0
    male_count = 0
    sec_list = []
    
    for i in range(len(nisit_female)) :  
        # check lecturer
        if nisit_female[i][1] == 'AAA' :
            female_count += 1
            # check sec inside check lecturer
            if (nisit_female[i][0] not in sec_list) :
                sec_list.append(nisit_female[i][0])
            
    for i in range(len(nisit_male)) :  
        # check lecturer
        if nisit_male[i][1] == 'AAA' :
            male_count += 1
            # check sec inside check lecturer
            if (nisit_male[i][0] not in sec_list) :
                sec_list.append(nisit_male[i][0])       
                
    # print output
    sec_str = ','.join(sec_list)
    if len(sec_list) == 1 :
        print('Section: ' + sec_str + ' --> ' + 'F = ' + str(female_count) + ', ' + 'M = ' + str(male_count))
    elif len(sec_list) > 1 :
        print('Sections: ' + sec_str + ' --> ' + 'F = ' + str(female_count) + ', ' + 'M = ' + str(male_count))
                
elif lecturer_in == 'BBB' :
    
    female_count = 0
    male_count = 0
    sec_list = []
    
    for i in range(len(nisit_female)) :  
        # check lecturer
        if nisit_female[i][1] == 'BBB' :
            female_count += 1
            # check sec inside check lecturer
            if (nisit_female[i][0] not in sec_list) :
                sec_list.append(nisit_female[i][0])
            
    for i in range(len(nisit_male)) :  
        # check lecturer
        if nisit_male[i][1] == 'BBB' :
            male_count += 1
            # check sec inside check lecturer
            if (nisit_male[i][0] not in sec_list) :
                sec_list.append(nisit_male[i][0])
                        
    # print output
    sec_str = ','.join(sec_list)
    if len(sec_list) == 1 :
        print('Section: ' + sec_str + ' --> ' + 'F = ' + str(female_count) + ', ' + 'M = ' + str(male_count))
    elif len(sec_list) > 1 :
        print('Sections: ' + sec_str + ' --> ' + 'F = ' + str(female_count) + ', ' + 'M = ' + str(male_count))
        
else :
    print('Not found')