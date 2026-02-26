# 1 : input nb.of rows -> find logic for storing 1D list

# 1.1 : Find logic
    # even row -> store reverse
    # odd row -> store normally
    # each row will store from rightmost to leftmost

n = int(input())
board = []
for row in range(n) :
    # case 1 : n = even -> check if row is even or odd
    if n % 2 == 0 :
        # row = even -> store normally
        if row % 2 == 0 :
            board += (input().split())
        # row = odd -> store reverse
        else :
            board += (input().split())[::-1]
    
    # case 2 : n = odd -> check if row is even or odd
    else :
        # row = even -> store reverse
        if row % 2 == 0 :
            board += (input().split())[::-1]
        # row = odd -> store normally
        else :
            board += (input().split())
            
# 1.2 : final result would get board reverse -> add start to index 0 and reverse list
board = ['start'] + board[::-1]

# 2 : input dices command -> split then analyze each cmds
dice_cmds = [int(e) for e in input().split()]
pos = 0
result = ''

# 3 : for loop : add pos for each dice
for dice in dice_cmds :
    pos += dice
    
    # 3.1 : check pos before checking cmds if win
    if pos >= (len(board) - 1):
        result += 'win'
        break
    
    # 3.2 : 'LADDER' and 'SNAKE' case -> update position
    if board[pos][0] in 'LS':
        pos = int(board[pos][1:])
        
        # check if win already
        if pos >= (len(board) - 1):
            result += 'win'
            break
        else :
            result += str(pos) + ' '
    
    # 3.3 : general case -> update position
    else :
        if pos >= (len(board) - 1):
            result += 'win'
            break
        else :
            result += str(pos) + ' '       
    
# 4 : print out result
print(result.strip())       