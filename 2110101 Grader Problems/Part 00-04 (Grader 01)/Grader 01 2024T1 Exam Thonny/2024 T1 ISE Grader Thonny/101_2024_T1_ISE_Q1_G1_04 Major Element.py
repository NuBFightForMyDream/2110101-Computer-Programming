# 1 : input info
numbers = [int(e) for e in input().strip().split()]

# 2 : check count -> add info 2 list 
count = []
num_counted = []

# 3 : for loop check info
for each_num in numbers :
    # check each element in list
    if each_num in num_counted :
        # add count to num_counted & add count
        pos = num_counted.index(each_num) # index pos
        count[pos] += 1 # add that pos 1
        
    else : # each_num not in num_counted
        # add new number & append count to 1
        num_counted.append(each_num)
        count.append(1)
        
# 4 : check if that number is element
major_element = []
for i in range(len(count)) :
    # major element is >= half of len 
    if count[i] >= (len(numbers) / 2) :
        # add element to major element
        major_element += [ num_counted[i] ]
        
# 5 : check if major element have 0 or more than 1 element
if len(major_element) == 0 or len(major_element) >= 2 :
    print('-1')
else : # have only 1 element
    print(major_element[0]) # print first element