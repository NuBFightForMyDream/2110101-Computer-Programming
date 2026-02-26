# 1 : input -> state,people
electoral_candidate = dict()
for i in range( int(input()) ) :
    # split info 
    info = input().split(',')
    # add key:val to dict
    electoral_candidate[info[0]] = int(info[1])
   
# 2 : add info to areas (key=county , val=state) dict
areas = []
for i in range( int(input()) ) :
    info = input().split(',')
    areas.append(info) # list of list
    
# 3 : input info -> county , state , rep_vote , dem_vote
rep_votes = dict() # 
dem_votes = dict()
for i in range( int(input()) ) :
    info = input().split(',')
    
    ## check if county,state in areas dict
    if info[0:2] in areas :
        # add key(states) , val(votes)
        ## check if name in dict already
        
        # case 1 : county:state in dict -> add rep&dem votes
        if (info[1] in rep_votes) and (info[1] in dem_votes) :
            rep_votes[info[1]] += int(info[2])
            dem_votes[info[1]] += int(info[3])
        
        # case 1 : county:state in dict -> define new rep&dem votes
        else :
            rep_votes[info[1]] = int(info[2])
            dem_votes[info[1]] = int(info[3])
      
# 4 : check each state in 2 dict -> add people to elec_rem & elec_dem
elec_rep = 0 # total electoral votes
elec_dem = 0 # total electoral votes
for each_state in electoral :
    # case 1 : republican wins -> add people to elec_rep
    if replubican_votes[each_state] > democrat_votes[each_state] :
        elec_rep += electoral[each_state]
    # case 2 : democrat wins -> add people to elec_dem
    else :
        elec_dem += electoral[each_state]
   
# check condition -> print info
print(str(elec_rep) + ':' + str(elec_dem))
if elec_rep > elec_dem :
    print('Republican wins')
elif elec_rep == elec_dem :
    print('Undecided')
else :
    print('Democrat wins')