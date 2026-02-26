# 1 : input info
info = input() # str
char_count = {} # create dict for storing info

# 2 : check first count
check = info[0] # str
count = 1 # first count

# 3 : for loop -> check each element in str
for i in range(len(info) - 1) :
    # check next
    
    # case 1 : if same char
    if check == info[i+1] :
        count += 1
        
    # case 2 : if not same char
    else :
        # update info to list
        char_count.update({count : check})
        # change count to 1 & check to that index
        check = info[i]
        count = 1
        
# out of for loop -> dont forget to check last member
if check == info[i+1] :
    count += 1
# whether if-else -> update info to dict
char_count.update({count : check})

# 4 : change dict to list (of list)