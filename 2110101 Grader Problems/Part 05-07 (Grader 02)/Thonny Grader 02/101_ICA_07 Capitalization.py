info = input().split(',') # list of str
str_out = ''
list_out = [] # for storing str

for i in range(len(info)) :
    info[i] = info[i].strip()
    for j in range(len(info[i])) :
        # check if first char -> change to upper 
        if j == 0 and info[i][j] not in ' <>*()^&%$#@!' :
            str_out += info[i][j].upper()
        # general case : lower
        elif info[i][j] not in ' <>*()^&%$#@!' : # normal char (not start & end)
            str_out += info[i][j].lower()
            
    # end loop -> add str to list
    list_out += [str_out]
    # reset str_out
    str_out = ''
    
print(' '.join(list_out))