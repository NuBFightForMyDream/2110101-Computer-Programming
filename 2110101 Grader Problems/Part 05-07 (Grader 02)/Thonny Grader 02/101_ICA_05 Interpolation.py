# check 2 pairs ; ex : we have 5 elements in list
# 1 , 3 , 5 , 7 , 9 => consider 1-3 , 3-5 , 5-7 , 7-9 -> check 4 times

old_list = [float(e) for e in input().split()] # list of float
avg_list = []

for pos in range(len(old_list)- 1 ) :
    avg = (old_list[pos] + old_list[pos+1]) / 2
    avg_list.append(avg)
    
step = 1
for ele in avg_list :
    old_list.insert(step , ele)
    step += 2