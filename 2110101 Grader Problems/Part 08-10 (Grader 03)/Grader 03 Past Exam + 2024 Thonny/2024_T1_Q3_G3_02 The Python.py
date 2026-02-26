# 1 : create dict for storing info
info = {}

# 2 : input info -> check if boss in bigboss
for i in range(int(input())) :
    boss , bigboss , amount = input().strip().split(',')
    # case 1 : have bigboss already -> update key:val
    if bigboss in info :
        info[bigboss].update({boss : int(amount)})
    # case 2 : never have bigboss -> create new key:val
    else : 
        # key , val of bigboss : list  boss(dict)
        info[bigboss] = {boss : int(amount)}

# 3 : check if each_boss is real bigboss
# !! checking each boss in each key will cover than checking each key on each boss
# Note : checking key (in info) then check boss will cover only 1 hierarchy
status_bigboss = {key:True for key in info} # start with everyone is bigboss

for each_boss , status in status_bigboss.items() : # checking key:val together
    for each_key in info :
        if each_boss in info[each_key] : # if that boss has bigboss
            status_bigboss[each_boss] = False # means there aren't bigboss
            info[each_key].update(info[each_boss]) # update new hierarchy to boss
      
# 4 : sort info then print (cover alphabetical case with same sales)
sales = []   
for each_key in info :
    if status_bigboss[each_key] == True :
        sales.append([-sum(info[each_key].values()) , each_key]) # sum values then *-1 for sorting
sales = sorted(sales) # sort info ascending
for [num , name] in sales :
    print('Boss' , name , str(-num)) # print info
    