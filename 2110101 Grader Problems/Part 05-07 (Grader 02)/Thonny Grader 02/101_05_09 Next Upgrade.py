# Try using list (of list) (Using 05_07 : Upgrade Idea)

# 1 : input stu_id , grade , uids
inp = input('Enter Student ID , Grade : ')
info = []
while inp != 'q' :
    info += [ [inp.split()[0] , inp.split()[1]] ] # add list (of list)
    inp = input('Enter Student ID , Grade : ')
# sort list (id)
info.sort()
uids = input('Enter Upgrade IDs : ').split()

# 2 : create grade list + index grade
original_grade = ['F','D','D+','C','C+','B','B+','A','A']

# 2.1 : for loop uids -> find each pos. in sublist
for ele in uids :
    # 2.1.1 : want to find pos. in list -> check cd.
    for i in range(len(info)) :
        if info[i][0] == ele : # info[i][0] is stu_id
            pos = i # int
            break
        
    # 2.1.2 : find info[pos][1] (stu_grade) in original_grade
    stu_grade = info[pos][1] # find grade first
        
    # 2.1.3 : then index for finding pos. in original_grade
    upgrade = original_grade.index(stu_grade) + 1 # int (move right 1 step)
        
    # 2.1.4 : change grade back to list (of list)
        # old grade (info[pos][1]) -> new grade (original_grade[upgrade])
    info[pos][1] = original_grade[upgrade]
        
# 3 : out of loop -> for loop -> print each sublist
for i in range(len(info)) :
    print( info[i][0] , info[i][1] )