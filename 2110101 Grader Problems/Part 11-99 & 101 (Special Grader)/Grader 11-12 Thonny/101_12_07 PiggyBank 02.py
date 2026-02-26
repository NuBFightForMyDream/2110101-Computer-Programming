# define class
class piggybank :
    # define initial fn
    def __init__(self) :
        # define dict for storing coins
        self.coins = dict()
        # key = valcoin , val = amount
    
    # define add method
    def add(self , v , n) :
        # check amount of coins first (should'nt > 100)
        if sum(self.coins.values()) + n > 100 :
            return False # coin full
        
        else : # general case -> add coin to piggy
            # check if having v in piggy
            if v not in self.coins :
                self.coins[float(v)] = n # add new key:val to dict
            else :
                self.coins[float(v)] += n
            # return True
            return True
        
    # define float magic method
    def __float__(self) :
        # return sum of money in piggybank
        total_value = 0
        for each_key in self.coins :
            total_value += each_key * self.coins[each_key]
            
        # check if total = 0
        if total_value == 0 : return 0.0
        return total_value
                
    # define str magic method
    def __str__(self) : # return str of dict
        # sort ascending by value of coin
        
        ## sorted to list of key -> index -> add to str
        str_coins = '{' # start with {
        list_valcoin = sorted(self.coins) # list of key
        
        for ele in list_valcoin :
            # add each key:val (formatted to str)
            str_coins += str(ele) + ':' + str(self.coins[ele]) + ', '
        
        # out of loop -> return str (strip ', ' then add })
        return str_coins.strip(', ') + '}'
    

# ----- Input Command Zone -----------------------------------------

# 1 : split cmd to list
cmd1 = input().split(';') 
cmd2 = input().split(';')

# 2 : create object -> call class
p1 = piggybank(); p2 = piggybank()

# 3 : evaluate str cmd
for c in cmd1: eval(c)
for c in cmd2: eval(c)    
    
    
    
    
    
    
    
    