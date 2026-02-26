# create class
class BigWallet :
    # define initial fn
    def __init__(self , NOTES) :
        # NOTES list will store type of banknotes
        self.notes = NOTES # list
        self.info_wallet = dict() # dict
        
        # for loop -> add key:val to dict
        for each_banknote in NOTES : 
            self.info_wallet[each_banknote] = 0
    
    # define valid_note for checking if having this banknote in list
    def valid_note(self , v) :
        return v in self.notes # return bool
    
    # define add money method (can done only if banknote in list)
    def add(self , v , n) :
        
        # case 1 : money in info_wallet
        if self.valid_note(v) == True : # have that banknote in wallet 
            # add num of banknotes to dict
            self.info_wallet[v] += n
            # no return
        
        # case 2 : money not in info_wallet
        if self.valid_note(v) == False :
            return 'Failed : Money Not in Wallet'
        
    # define total fn
    def total(self) : # return total money in info_wallet
        total = 0
        for each_key in self.info_wallet :
            total += self.info_wallet[each_key] * each_key
        return total
        
    # define lt magic method (for sorting)
    def __lt__ (self , rhs) :
        return self.total() < rhs.total() # dont forget ()
            