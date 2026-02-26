# 1 : input winner & loser -> add to list or set
    # set is better in this task -> for receiving repeated info
winner = set()
loser = set()
for i in range( int(input()) ) :
    win , lose = input().split()
    # add info to set
    winner.add(win) # set use add (not append)
    loser.add(lose)
    
# 2 : check element in loser set -> if found , delete element in set
for ele in loser : 
    if ele in winner :
        winner.remove(ele) # final result = set
        
# 3 : print sorted
print(sorted(winner)) # sorted(set) = list -> print list
    