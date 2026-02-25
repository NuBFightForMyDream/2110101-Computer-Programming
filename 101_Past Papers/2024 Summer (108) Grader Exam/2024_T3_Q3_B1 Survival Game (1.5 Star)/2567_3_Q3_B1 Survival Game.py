#
# 2567_3_Q3_B1: 2567_3_Q3_B1: Survival Game 
#

survival_info = {} # list of list

info = input().split()
    # even pos (0,2,4,..) is name , odd pos (1,3,5,...) is minutes stay

# add info to survival_info
for i in range(0 , len(info) , 2) :
    # i will be name , i+1 will be minutes_stay
    if info[i] in survival_info :
        # add minutes
        survival_info[ info[i] ] += int(info[i+1])
        
    else :
        survival_info[ info[i] ] = int(info[i+1])

most_survival = []# list of list
for key in survival_info :
    most_survival += [ [-survival_info[key] , key] ] # time minus for descending
    
most_survival = sorted(most_survival)

count = 1 ; out = ""
for sublist in most_survival :
    if count <= 3 : 
        out += sublist[1] + " "
        count += 1
    else :
        break
    
print(out)
    

        