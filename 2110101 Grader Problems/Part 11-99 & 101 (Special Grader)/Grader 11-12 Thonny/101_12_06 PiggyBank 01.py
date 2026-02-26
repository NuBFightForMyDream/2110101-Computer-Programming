# 1 : define class PiggyBank
class piggybank:
    # define initial fn
    def __init__(self) : # define var. for storing info
        # define dict with key = coin , val = 0 first
        self.coin1 = {1:0}
        self.coin2 = {2:0}
        self.coin5 = {5:0}
        self.coin10 = {10:0}
    
    # define 4 methods : add coins to val
    def add1(self , n):
        self.coin1[1] += n
        
    def add2(self, n):
        self.coin2[2] += n
        
    def add5(self , n):
         self.coin5[5] += n
        
    def add10(self , n) :
        self.coin10[10] += n
        
    # define int magic method -> sum each value
    def __int__(self) :
        total = 0 # summing all coins
        # define list of dict -> sum each element
        list_coin = [self.coin1 , self.coin2 , self.coin5 , self.coin10]
        # nested for loop -> asum value
        for each_dict in list_coin :
            for each_key in each_dict : # for key in each_dict
                total += (each_key) * (each_dict[each_key]) # key x val
        # out of loop -> return total
        return total
    
    # define lessthan method (for sorting later)
    def __lt__ (self , rhs) : # call magic method , cmd : method_name(var.)
        if int(self) < int(rhs) : return True
        return False # else amount1 > amount2
    
    # define str magic method -> return str in dict form
    def __str__(self):
        # create bigdict by update each subdict
        str_allcoin = '{' # create str out
        for each_dict in [self.coin1 , self.coin2 , self.coin5 , self.coin10] :
            # add key:val to str
            for key in each_dict :
                str_allcoin += str(key) + ':' + str(each_dict[key]) + ', '
        # return format
        return str_allcoin.strip(', ') + '}'

# --------------------------------------------------------
# 1 : input 2 commands -> split to list
cmd1 = input().split(';')
cmd2 = input().split(';')
# 2 : define object
p1 = piggybank(); p2 = piggybank()
# 3 : for loop each char in list_cmd -> evaluate each char
for c in cmd1: eval(c) # processing string to cmds
for c in cmd2: eval(c)