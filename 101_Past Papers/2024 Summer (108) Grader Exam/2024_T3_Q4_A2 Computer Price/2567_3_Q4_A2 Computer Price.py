#
# 2567_3_Q4_A2: 2567_3_Q4_A2: Computer Price 
#

# 1 : input info
val_A , val_B , val_C , val_D , val_E = [int(e) for e in input().split()]
value = [] # list of list

# 2 : input info
info = input().split() # info = ['ROOM_NUM' , 'INFO_IN']
while info[0] != 'END' :
    # calculate value of the room first
    total_value = val_A * info[1].count('A') + val_B * info[1].count('B') +val_C * info[1].count('C') +val_D * info[1].count('D') + val_E * info[1].count('E') 
    
    # store value to list
    value += [ [-total_value , info[0] ] ]
    
    # enter another info
    info = input().split()
    
# 3 : sort list the get output
value = sorted(value)

# 4 : get output
print(value[0][1])
    