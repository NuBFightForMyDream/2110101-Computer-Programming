# 1 : input & create empty dict
info = input()
animals = {}

# 2 : while loop input
while info != 'q' :
    # 2.1 : split info
    name , atype = info.split(', ')[0] , info.split(', ')[1]
    
    # 2.2 : check if info in dict
    if atype not in animals :
        animals[atype] = [name]
        
    else : # if have elements -> add elemnt to value (list)
        animals[atype] += [name]
        
    # 2.3 : input info
    info = input().strip()
    
# 3 : for loop key -> print each elements & join value to str
for key in animals :
    print(f"{key}: {', '.join(animals[key])}")