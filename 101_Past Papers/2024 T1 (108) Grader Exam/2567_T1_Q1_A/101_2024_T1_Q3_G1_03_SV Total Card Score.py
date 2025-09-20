# 1 : input info & strip
info_cards = input().strip('|').split('|') # list
total_points = 0

# 2 : check each info
for ele in info_cards :
    # 1-2 first char = value , ♠ ♥ ♦ ♣ = suit
    
    ## consider only value
    value_list = ['0','A','2','3','4','5','6','7','8','9','10']
    
    if len(ele) == 2 :
        # check 2-10
        if ele[0] in 'JQK' : total_points += 10
        else : total_points += value_list.index(ele[0])
            
    else : # len(ele) == 3 -> 10 only
        total_points += 10
  
# 3 : print total
print(total_points)