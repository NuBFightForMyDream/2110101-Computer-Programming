# 1 : define fn
def print_seats(assignments , n_rows , n_cols) :
    # assignments = list of list
    # EX : [['PS',6],['CP',3],['SS',1],['TC',5]]
    
    # 1 : define empty nested list first -> nested loop and add each element
    seats_out = []
    for row in range(n_rows) :
        # outer loop -> add row
        sub_seat = []
        # inner loop -> add column
        for col in range(n_cols) :
            sub_seat.append('--')
        seats_out.append(sub_seat)
    # !! Don't craeting by [[]*row]*col cuz it means you're making pair list
    
    # 2 : for loop -> check pos for each element
    for [name , pos] in assignments :
        # find formula to add name to pos -> -1 first (cuz seats starts at 0)
        row = (pos-1) // n_cols # row by //
        col = (pos-1) % n_cols # col by %
    
    # 3 : change each element form '--' to 'XX'
        seats_out[row][col] = name
        
    # 4 : print format
    for rows in seats_out : # rows = list of str
        print('| ' + ' | '.join(rows) + ' |')

exec(input())