# 1 : input & split info
info = dict()
for i in range( int(input()) ) :
    # input info 
    boss , bigboss , sales = input().strip().split(',')
    # check if bigboss in dict
        # case 1 : bigboss in dict (have bigger boss) -> update dict in value
    if bigboss in info :
        info[bigboss].update( {boss : int(sales)} )
        # case 2 : bigboss not in dict -> add new key:val in dict
    else :
        info[bigboss] = { boss : int(sales) }

# 2 : define recursive fn for checking bigboss
def find_bigboss(boss) :
    # Logic : if boss have bigger chain -> find biggest
    # check each boss -> if boss in value (chain) -> find bigger boss
    for each_boss , chain in info.items() : # each_boss = key , subboss = val (set of dict)
        
    # case 1 : find boss in value -> find bigger boss -> call recursive fn again
        if boss in chain : # find bigger boss : call fn again until got bigboss
            return find_bigboss(each_boss) # find bigboss of boss we're checking        
    
    # case 2 : if can't find bigger boss -> they are bigboss
    return boss # return bigboss
    
# 3 : create total_sales dict -> add only bigboss
total_sales = {}

# check all values in bigdict -> find bigboss (check all pairs)
for each_boss , chain in info.items() : # chain = dict
    for subboss , amount in chain.items() :
        # check all values in bigdict -> find bigboss
        bigboss = find_bigboss(each_boss)
        
        # check if bigboss in dict
        if bigboss not in total_sales :
            total_sales[bigboss] = 0
        # dont have bigboss in total_sales
        total_sales[bigboss] += amount
        
# 4 : sort & print
sales = sorted([(-total, boss) for boss, total in total_sales.items()])
for total, name in sales:
    print('Boss', name, -total)       