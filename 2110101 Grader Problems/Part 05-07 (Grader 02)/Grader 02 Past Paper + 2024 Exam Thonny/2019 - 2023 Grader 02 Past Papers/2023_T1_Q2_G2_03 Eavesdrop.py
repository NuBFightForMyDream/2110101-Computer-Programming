# 1 : input character
char_list = []
for i in range(int(input())) :
    inp = input()
    char_list.append(inp)
    
# 2 : while loop input & add string (dont forgot to \n )
conver = ''

while True : # still input
    info = input() # input info & store to conver
    # add all to str
    conver += info + '\n'
    # check if story ends
    if info == 'END' :
        break
    
script = conver.split('*')

# 3 : for loop -> check if it starts with *name
found = False # define false for wrong novel

for ele in script :
    # find pos of ':' -> for searching 
    colon = ele.find(':')
    # find end -> before second '"'
    # let's find first "
    dbq_pos = ele.find('"')
    next_dbq_pos = ele.find('"' , dbq_pos + 1) # start from next index of dbq
    
    # check name (before :) if it's in char_list
    if ele[0:colon] in char_list : # check name (before :) if it's in char_list
        found = True
        out_text = ele[0 : next_dbq_pos + 1] # +1 cuz we need second " in conver.
        print(ele[0:next_dbq_pos+1].strip()) # strip for removing \n

# 4 : check if it's wrong novel
if found == False :
    print('Maybe wrong novel')