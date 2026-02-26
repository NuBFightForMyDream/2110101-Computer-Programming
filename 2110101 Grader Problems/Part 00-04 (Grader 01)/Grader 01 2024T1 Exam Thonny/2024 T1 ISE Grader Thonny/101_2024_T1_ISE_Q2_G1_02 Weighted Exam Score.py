# 1 : input tasks per grader , percentage , points (all are integers)
task_g1 , task_g2 , task_g3 = [int(e) for e in input().split()]
percent_g1 , percent_g2 , percent_g3 = [int(e) for e in input().split()]
info_grader = [int(e) for e in input().split()]

# 2 : split info & calculate -> slice list
g1_info = info_grader[0 : task_g1 : 1]
g2_info = info_grader[task_g1 : task_g1+task_g2 : 1]
g3_info = info_grader[task_g1+task_g2 : task_g1+task_g2+task_g3 : 1]

# 3 : check constrain

# case 1 : # exam not equal to #total
if (task_g1 + task_g2 + task_g3) != len(info_grader) :
    print('Invalid data')

# case 2 : sum of weights not equal 100
elif (percent_g1 + percent_g2 + percent_g3) != 100 :
    print('Invalid data')
    
# case 3 : general case -> calculate score with weighted
else :
    total_g1 = sum(g1_info) * percent_g1
    total_g2 = sum(g2_info) * percent_g2
    total_g3 = sum(g3_info) * percent_g3
    
    # calculate average
    average = (total_g1 + total_g2 + total_g3) / (100 * len(info_grader))
    print( round(average , 2) )