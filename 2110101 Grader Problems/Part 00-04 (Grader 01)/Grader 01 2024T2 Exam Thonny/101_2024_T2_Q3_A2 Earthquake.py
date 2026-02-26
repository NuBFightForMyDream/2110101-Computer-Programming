# 1 : define initial var.
delta_distance = int(input())

v_child = 2
v_parent = 2 * v_child
time_passed = 0

# check if found at start
if delta_distance <= 50 :
    print(time_passed , delta_distance) # time_passed = 0

# otherwise , calculate delta_distance
else : 
    while delta_distance > 50 :
        # calculate each second
        ## update delta_distance
        delta_distance -= (v_child + v_parent)
        time_passed += 1 # add 1 second for each time
        
        ## print output for every 1 minutes (to 5 minutes)
        if (time_passed % 60 == 0) and (time_passed <= 300) :
            print(time_passed // 60 , delta_distance)
    
    # out of loop -> print latest time_passed & delta_distance (should < 50)
    print((time_passed // 60) + 1 , delta_distance) # +1 for ceiling  