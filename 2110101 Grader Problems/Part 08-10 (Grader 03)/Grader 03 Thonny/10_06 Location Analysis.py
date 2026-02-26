# 1 : create dict & list
gps = {} # dict for storing info
ids = []# list for printing name by sequence

# 2 : input info
for i in range( int(input()) ) :
    info = input()
    # split info
    ID = info.split(': ')[0]
    location = (info.split(': ')[1]).split(', ') # split first for str -> split 2nd for list
    # append id to ids list
    ids.append(ID)
    # add key:value to dict
    gps[ID] = location
    
# 3 : check input
check = input().strip()
# 3.1 : create list for storing ppl found
found = []
# 3.2 : for loop outer -> check element in value 
for ele in gps[check] :
    # for loop each key in dict
    for key in gps :
        # make conditions
        if (ele in gps[key]) and (key != check)\
            and key not in found :
            found.append(key)
    
# 4.2 : check ppl found in list
if found != [] :
    # for loop -> if found ele in ids -> print
    for ele in ids :
        if ele in found :
            print(ele)
else :
    print('Not Found')
    
