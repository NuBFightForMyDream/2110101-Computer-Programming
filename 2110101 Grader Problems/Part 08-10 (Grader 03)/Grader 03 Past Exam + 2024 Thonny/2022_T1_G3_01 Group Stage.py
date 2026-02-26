football_team = dict() # dict for storing key:val (key = country , val = list of name)
team_names = set() # for storing names (check)

for i in range(int(input())) :
    info = input().split()
    # check if element in dict
    if info[1] not in football_team :
        football_team[ info[1] ] = [info[0]]
    else :
        football_team[ info[1] ].append(info[0])
    # store info in set (set finds faster than list)
    team_names.add(info[0])
    
# input info
info = input().split() # str -> list
while info != ['q'] :
    # create False cd. -> break if it's False
    countries_list = [] # for case 2 -> check if name repeated
    countries_set = set()
    imposter = False # bool for checking if sus name in list
    
    # case 1 : naem not in set
    for ele in info :
        if ele not in team_names :
            imposter = True
            print('Not OK')
            break
        # case 2 : having same country (still check inside ele)
        # for loop key in dict -> find if ele in val
        for key in football_team :
            if ele in football_team[key] : # ele in value -> append name to list and set
                countries_list.append(key)
                countries_set.add(key)
    # end loop -> check if name is repeated (by sort both & check equal) -> not empty list or set
    if imposter == False : 
        if sorted(countries_list) == sorted(countries_set) :
            print('OK')
        else :
            print('Not OK')
        
    # input info
    info = input().split()           