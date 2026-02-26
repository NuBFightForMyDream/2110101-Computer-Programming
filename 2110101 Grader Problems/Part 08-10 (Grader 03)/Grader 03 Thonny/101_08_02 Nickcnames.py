# 1 : input range
info = {}
nb = int(input())

# 2 : for loop -> input name
for i in range(nb) :
    ## Logic : create double elements (name:nick & nick:name)
    
    # 1.1 : input & split
    name , nick = input().strip().split()

    # 1.2 : add elements (check key -> if key not in dict -> will add automatically)
    info[name] = nick # name = key , nick = value
    info[nick] = name # nick = key , name = value
    
# 3 : for loop -> input check & check key
nb_check = int(input())
for j in range(nb_check) :
    check = input()
    
    # 3.1 : if key in dict -> print dict(from key)
    # No Need to for loop check
    if check in info :
        print(info[check]) # print value from check
    
    # 3.2 : else -> print 'Not Found'
    else :
        print('Not found')