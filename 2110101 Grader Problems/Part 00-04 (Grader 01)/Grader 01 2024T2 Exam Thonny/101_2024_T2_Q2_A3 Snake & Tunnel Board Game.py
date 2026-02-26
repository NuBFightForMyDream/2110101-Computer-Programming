# 1 : input & transform 2D table to 1D list
N = int(input())

board = []
for line in range(N) :
    # input info for each board
    
    # for all case N : even row = normal , odd row = reverse
    
    if line % 2 == 0 : # even row = normal input
        board += input().strip().split()
        
    elif line % 2 != 0 : # odd row = reverse input
        board += (input().strip().split())[::-1]
        
# !! dont forget to add start before pos. 1
board = ['start'] + board

# 2 : do logic for snake & ladder board

# 2.1 : input cmd
cmds = [int(e) for e in input().split()]
pos = 0 # represents position for each dice roll
rolls = [] # tol_sed_leaw list for each pos.

for dice in cmds :
    # check first if already win
    if pos >= len(board) - 1 :
        rolls += ['win']
        break
        
    # otherwise -> check that position if 'T' , 'S'
    else :
        # add new roll first
        pos += dice
        
        # check first if already win
        if pos >= len(board) - 1 :
            rolls += ['win']
            break
    
        # check if 'T' or 'S'
        if board[pos][0] in 'TS' : # Ex ; 'T13' or 'S4'
            # check if already win
            if pos >= len(board) - 1 :
                rolls += ['win']
                break
            # otherwise , update position & cmd
            else : 
                pos = int(board[pos][1:])
                
                # check if already win
                if pos >= len(board) - 1 :
                    rolls += ['win']
                    break
            
                else :
                    rolls += [pos]
                
        # otherwise , add cmd
        else :
            # check if already win
            if pos >= len(board) - 1 :
                rolls += ['win']
                break
            # otherwise , update position & cmd
            else : 
                rolls += [pos]
        
# 3 : out of loop , print out cmd
print(*rolls)