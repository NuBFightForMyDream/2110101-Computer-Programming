# 1 : input filename 
filename1 = input()
filename2 = input()
filename3 = input()

# 2 : open file
fn1 = open(filename1 , 'r') # courses
fn2 = open(filename2 , 'r') # teachers
fn3 = open(filename3 , 'r') # database

# 3 : create empty dict for storing info
info_courses = {}
info_teachers = {}

# 4 : for loop line in file 1&2 -> sooring in dict
for line in fn1 :
    data = line.strip().split(',')
    tag = data[0] ; codename = data[1]
    info_courses[tag] = codename # key = tag , value = name
fn1.close() # close file
    
for line in fn2 :
    data = line.strip().split(',')
    tag = data[0] ; name = data[1]
    info_teachers[tag] = name # key = tag , value = name
fn2.close() # close file
    
# 5 : for loop line in database -> check each line in database
for line in fn3 :
    data = line.strip().split(',')
    tag1 = data[0] ; tag2 = data[1]
    # check if info in dict -> if found , print
    if (tag1 in info_courses) and (tag2 in info_teachers) : # find key in dict
        print(info_courses[tag1] + ',' + info_teachers[tag2] )
    # if not -> print 'record error'
    else :
        print('record error')
fn3.close() # close file