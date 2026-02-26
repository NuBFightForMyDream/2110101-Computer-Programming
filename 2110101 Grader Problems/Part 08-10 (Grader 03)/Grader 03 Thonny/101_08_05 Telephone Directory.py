# 1  : define empty dict
tel_dict = {}

# 2 : for loop -> input info
for i in range(int(input())) :
    # 2.1 : strip info 
    info = input().strip()
    
    # 2.2 : define info for splitting
    fullname = (info.split()[0] + ' ' + info.split()[1])
    phonenum = info.split()[2]
    
    # 2.3 : add key:value & value:key in empty dict (looping)
    tel_dict[fullname] = phonenum
    tel_dict[phonenum] = fullname
    
# 3 : for loop -> input check 
for i in range(int(input())) :
    # 3.1 : strip first
    check = input().strip()
    
    # checking if found -> print format
    if check in tel_dict :
        print(f"{check} --> {tel_dict[check]}")
    else : 
        print(f"{check} --> Not found")