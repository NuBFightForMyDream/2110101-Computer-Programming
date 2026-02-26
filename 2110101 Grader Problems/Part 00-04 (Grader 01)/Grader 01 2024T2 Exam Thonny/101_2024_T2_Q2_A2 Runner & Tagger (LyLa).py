# 1 : input info
a_tagger , a_runner , delta_distance = [float(e) for e in input().split()]

# 2 : analysis

## if a_runner >= a_tagger => not possible in every case
## assume that two person starts at velocity = 0
## if not -> while loop until tagger reach runner

# case 1 : a_runner >= a_tagger = 'Not possible'
if a_runner >= a_tagger :
    print('Not possible')
    
# case 2 : tagger can reach runner
else :
    # given variables for calculating distance
    p_runner_old = delta_distance ; p_runner_new = delta_distance
    p_tagger_old = 0 ; p_tagger_new = 0
        # Note : given p_tagger as 0 , so p_runner will + delta_distance from p_tagger
    v_runner_old = 0 ; v_runner_new = 0
    v_tagger_old = 0 ; v_tagger_new = 0
    
    time_passed = 0

    # while loop , calculate distance & velocity
    while delta_distance > 0 :
        
        # calculate velocity
        v_runner_new = v_runner_old + (a_runner * 1)
        v_tagger_new = v_tagger_old + (a_tagger * 1)
        
        # calculate distanced traveled
        p_runner_new += v_runner_old + 0.5*(v_runner_new - v_runner_old)
        p_tagger_new += v_tagger_old + 0.5*(v_tagger_new - v_tagger_old)
        
        # calculate delta distance
        delta_distance = p_runner_new - p_tagger_new
        
        # add time passed
        time_passed += 1
        
        # update v_old has value v_new for both runner & tagger
        v_runner_old = v_runner_new
        v_tagger_old = v_tagger_new
        
    # print out value
    print(time_passed , round(p_tagger_new , 2) )