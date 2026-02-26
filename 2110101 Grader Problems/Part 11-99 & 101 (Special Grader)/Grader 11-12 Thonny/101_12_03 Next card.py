# define class
class Card :
    # define initial fn
    def __init__ (self , value , suit) :
        # annouce var.
        self.value = value
        self.suit = suit
    # define str magic method
    def __str__ (self) :
        return '(' + self.value + ' ' + self.suit + ')'
    
    # define next1 fn -> return next pos. card (not editing object)
    def next1(self) :
        # define list
        value_list = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        suit_list = ['club','diamond','heart','spade']
        # check if suit is spade -> +1 value & change suit to club
        if self.suit == 'spade' :
            # define next_valpos (int) then index in list
            next_valpos = (value_list.index(self.value) + 1 )% len(value_list) # int
            next1_val = value_list[next_valpos]
            # change suit to club
            next1_suit = 'club'
            # return value
            return '(' + next1_val + ' ' + next1_suit + ')'
        
        else : # general case
            # define next_suitpos (int) -> index in list
            next_suitpos = suit_list.index(self.suit) + 1
            next1_suit = suit_list[ next_suitpos ]
            # no need to change value -> return value
            return '(' + self.value + ' ' + next1_suit + ')'
            
    # define next2 fn -> return next pos. card (editing object)
    def next2(self) :
        # define list
        value_list = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        suit_list = ['club','diamond','heart','spade']
        # check if suit is spade -> +1 value & change suit to club
        if self.suit == 'spade' :
            # define next_valpos (int) then index in list
            next_valpos = (value_list.index(self.value) + 1 )% len(value_list) # int
            self.value = value_list[next_valpos] # change object directly
            # change suit to club
            self.suit = 'club'
            # return value (str)
            return '(' + self.value + ' ' + self.suit + ')'
        
        else : # general case
            # define next_suitpos (int) -> index in list
            next_suitpos = suit_list.index(self.suit) + 1
            self.suit = suit_list[ next_suitpos ] # change object directly
            # no need to change value -> return value
            return '(' + self.value + ' ' + self.suit + ')'

# ----------------------------- Input test Zone ------------------------

# 1 : input info
n = int(input())
cards = [] # list of object
for i in range(n):
    value, suit = input().split() # split & append object to list of object
    cards.append(Card(value, suit))
    
# 2 : test next1 fn
for i in range(n):
    print(cards[i].next1())
print("----------")

# 3 : test next2 fn
for i in range(n):
    print(cards[i])
print("----------")

# 4 : test double next2 fn (return 2 next card & editing object)
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i]) 