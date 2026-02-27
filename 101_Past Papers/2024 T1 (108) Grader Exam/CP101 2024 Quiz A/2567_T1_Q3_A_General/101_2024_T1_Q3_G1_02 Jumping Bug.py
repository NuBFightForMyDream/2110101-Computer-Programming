# Dr.Somchai recommended that do case with no hole first (got 80%)

# 1 : input info (each line)
total_dist = float(input())
jump_factor = float(input())
end_gap = float(input())
pit_start = float(input())
pit_end = float(input())

round_jump = 0

# 2 : do case with no hole first -> 80% of testcases
if pit_start == -1 and pit_end == -1 : # No Hole
    
    # define var. for first jump
    length = 0 # total
    now = jump_factor * total_dist # first jump -> no need to check left_distance
    
    # while loop -> check if not finished
    while length < (total_dist - end_gap) :
        # add previous jump first
        round_jump += 1
        
        # update length & left distance
        length += now
        dist_left = (total_dist - length)
        
        # calculate next jump distance (since 2nd jump -> consider left distance only)
        now = jump_factor * dist_left
        
    # out of loop -> print round that jump
    print(round_jump)   
    
# 3 : do case with hole -> 20% of testcases
else : # Hole
    
    # calculate first jump (for sure with no hole at first jump)
    length = 0
    now = jump_factor * total_dist # for first jump
    
    # while loop -> check if not finished
    while length < (total_dist - end_gap) :
        # add previous jump first
        round_jump += 1
        # update length & dist_left
        length += now
        dist_left = (total_dist - length)
        
        # check if it's hole on next jump
        if pit_start <= length < pit_end : # Hole on next jump
            now = pit_end - length
            length = pit_end
        else : # Not a hole on next jump
            # update now distance
            now = jump_factor * dist_left

    print(round_jump)