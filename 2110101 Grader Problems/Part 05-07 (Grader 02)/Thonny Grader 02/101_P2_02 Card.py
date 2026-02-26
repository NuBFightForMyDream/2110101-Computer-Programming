# 1 : define fn for reading value
def diff_card(info1 , info2):
    # 1.1 : read first digit of card
    value_card = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    set_card = ['C','D','H','S']
    # 1.2 : check if first digit is same or not
    
    # case 1 : same first digit -> consider diff only second digit (set_card)
    if info1[0] == info2[0] : 
        diff = 0 + ( set_card.index(info1[1]) - set_card.index(info2[1]) )
        
    # case 2 : different first digit -> consider diff first digit only
    elif info1[0] != info2[0] :
        diff = ( value_card.index(info1[0]) - value_card.index(info2[0]) ) + 0
        
    # 1.3 : return diff
    return diff # int

# 2 : consider card in our hand
cards_info = input('Enter Cards Info In Your Hand : ').strip() # strip for error 
diff_out = ''

# 2.1 : check loop -> Logic : loop until len - 3 (cuz consider i,i+1,i+2,i+3) , step 2
for i in range(0 , len(cards_info) - 2 , 2) :
    # 2.1.1 : check value positive or negative
    diff = diff_card( cards_info[i:i+2] , cards_info[i+2:i+4] ) # (i&i+1) <-> (i+2 , i+3)
    if diff > 0 :
        diff_out += '+' + str(diff)
    else :
        diff_out += str(diff)
        
# 3 : out of loop -> print diff (strip too)
print(diff_out.strip())
