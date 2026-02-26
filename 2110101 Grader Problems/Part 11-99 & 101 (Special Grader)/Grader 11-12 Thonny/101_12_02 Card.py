# define class
class Card:
    # 1 : define initial fn
    def __init__(self , value , suit) :
        # annouce var. in class (no need to return)
        self.value = value
        self.suit = suit
        
    # 2 : define str method (return str)
    def __str__(self) :
        # return str in form : (value card) 
        return '(' + self.value + ' ' + self.suit + ')'
    
    # 3 : define getScore method (return point)
    def getScore(self) :
        # return point (int) of each card (see value)
        if self.value == 'A' : return 1
        elif self.value in 'JQK' : return 10
        else : # 2-9 Card -> return value of card
            return int(self.value)
        
    # 4 : define sum fn (sum 2 cards (objects))
    def sum(self , other) : # self , other = object
        # update value to new var. in class
        ## call getScore fn (Card. cuz inside same class)
        value_total = Card.getScore(self) + Card.getScore(other)
        # return & mod 10
        return value_total % 10
    
    # 5 : define lessthan (__lt__) fn for sorting later
    def __lt__(self , rhs) :#  check if val_card1 < val_card2
        
        # 1 : create list for index pos. from var. (suit list & value list)
        suit_list = ['club','diamond','heart','spade']
        value_list = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        
        # 2 : indexing pos. from list
        pos_suit1 = suit_list.index(self.suit)
        pos_suit2 = suit_list.index(rhs.suit)
        pos_val1 = value_list.index(self.value)
        pos_val2 = value_list.index(rhs.value)
        
        # 3 : check condition (check value then suit)
        
        # case 1 : value1 < value2 -> return True
        if pos_val1 < pos_val2 : return True
        # case 2 : value1 == value2 -> check suit
        elif pos_val1 == pos_val2 :
            if pos_suit1 < pos_suit2 : return True
            else : return False
        # case 3 : value1 < value2 -> return False
        else : return False
# -------------------------------------------------------
## calling object zone

# 1 : input info & store in list
n = int(input())
cards = [] # list of objects [Cards() , Cards() , ...]
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit)) # append object to list
    
# 2 : output #1 : get each card score (call getScore method)
for i in range(n):
    print(cards[i].getScore())
print("----------")

# 3 : output #2 : get sum of each pair cards (call sum method)
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")

# 4 : sort card (call __lt__ method)
cards = sorted(cards)

# 5 : print each card info (call __str__ method)
for i in range(n):
    print(cards[i])