# 1 : input info

# 1.1 : rating info first
info_rate = {} # dict
names = set() # set for checking None rate
# input info
rate_in = input().split()
while rate_in != ['END'] :
    # check sign first
    if (rate_in[1][-1] == '+') or (rate_in[1][-1] == '-') : # check +/-
        rate_in[1] = rate_in[1][:-1] # no need +/-
    
    # add names to set
    names.add(rate_in[0])
    
    # check if rate in dict
    if rate_in[1] not in info_rate :
        info_rate[rate_in[1]] = [rate_in[0]] # add key:val
    else : # rate in dict -> append list
        info_rate[rate_in[1]].append(rate_in[0])
        
    # still input info
    rate_in = input().split()
    
# add -> define fn for find name of bond
def find_pos(bondname) :
    for k in range(len(bondname)) :
        if '1' <= bondname[k] <= '9' : return k
        
# 1.2 : input bond info
bond_info = {'None':0} # dict -> store info for output (add key:val of None first)
bond_in = input().split()
total_money = 0 # for calculate percentage

while bond_in != ['END'] :
    # split element -> need only name -> call fn for pos
    pos = find_pos(bond_in[0])
    name = bond_in[0][0:pos] 
    money = int(bond_in[1])
    
    # add money to total
    total_money += money
    
    # check if name in dict -> for loop key -> check ele in val
    for key in info_rate :
        if name in info_rate[key] : # if name in val -> check if name in bond_info?
            if key not in bond_info :
                bond_info[key] = money; break
                # add key:val to dict
            else :
                bond_info[key] += money; break # key = group , val = money
        
        else : # name not in val -> check if name not in set
            if name not in names :
                # check if None alrady have in dict 
                bond_info['None'] += money 
                break # find new input
            
    # still input
    bond_in = input().split()
    
# 3 : for loop -> check name & print info
for rating in ['AAA','AA','A','BBB','BB','B','CCC','CC','C','D','None'] :
    # loop each element -> if found ele in dict -> print info
    if rating in bond_info :
        # calculate percentage
        percentage = round( (bond_info[rating] / total_money * 100) , 2)
        # print info -> key , val , percentage
        print(f"{rating} {bond_info[rating]} {percentage}%")
        