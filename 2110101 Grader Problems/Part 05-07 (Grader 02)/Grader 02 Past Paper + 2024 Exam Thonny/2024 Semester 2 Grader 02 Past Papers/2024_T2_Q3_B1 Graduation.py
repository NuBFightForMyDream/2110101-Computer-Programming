# 1 : create var,
graduation_info = [] # storing nisits info

first_honour_id = [] # storing list of list [gpax , stu_id]
second_honour_id = [] # storing list of list [gpax , stu_id]
general_id = []

grades = ['F','D','D+','C','C+','B','B+','A'] # using for index

# 2 : while loop -> check info
nisit_info = input()

while nisit_info != '-1' :
    # split for info
    stu_id , gpax , lowest_grade , gened_unsatisfied , year_graduated = nisit_info.split()
    # change type
    gpax = float(gpax) ; stu_id = int(stu_id)
    year_graduated = float(year_graduated)
    pos_lowest_grade = grades.index(lowest_grade) # check if index < 3 (C)
    
    # check 1st honour degree
    if (gpax >= 3.60 and pos_lowest_grade >= 3 and gened_unsatisfied == 'N' and year_graduated <= 4) :
        first_honour_id.append( [-gpax , stu_id] ) # gpax will sort from less to more (descending order)
        
    # check 2nd honour degree
    elif ((3.25 <= gpax < 3.60) and pos_lowest_grade >= 3 and gened_unsatisfied == 'N' and year_graduated <= 4) :
        second_honour_id.append( [-gpax , stu_id] )# gpax will sort from less to more (descending order)
        
    else :
        general_id.append(stu_id)
        
    # still input info
    nisit_info = input()
    
# 3 : after done loop , sort id then check and print
# 3.1 : sort list

first_honour_id = sorted(first_honour_id)
second_honour_id = sorted(second_honour_id)
general_id = sorted(general_id)

### using lambda function
## first_honour_id = sorted(first_honour_id, key=lambda infos: (-infos[0], infos[1]) )
## second_honour_id = sorted(second_honour_id, key=lambda infos: (-infos[0], infos[1]) )
    # define var. as ele
    # using lambda by define sorted( ... , key = ... ) (key = lambda)
    # we want to sort list so we define x as each element in list
    # we sort : lambda ele : [ -ele[0] , ele[1] ]  as format in list (of list)
    # - ele[0] for descending order , ele[1] for alphabetically

# check output
if len(first_honour_id) > 0 :
    print('1st Honour Degree') # output said '1'
    for [gpax , stu_id] in first_honour_id :
        print(stu_id)

if len(second_honour_id) > 0 :
    print('2nd Honour Degree')
    for [gpax , stu_id] in second_honour_id :
        print(stu_id)
        
if len(general_id) > 0 :
    print('General Degree')
    for stu_id in general_id :
        print(stu_id)