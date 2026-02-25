#
# 2567_3_Q5_A2: 2567_3_Q5_A2: Max. Total Component Values 
#

# 1 : input info & set variable first
val_A , val_B , val_C , val_D , val_E = [int(e) for e in input().split()]

total_A , total_B , total_C , total_D , total_E = 0 , 0 , 0 , 0 , 0

# 2 : input info & calculate value
info = input().split()

while info[0] != 'END' :
    # split info
    room_num = info[0]
    computer_info = info[1]
    
    # calculate A , B , C , E components
    for each_value in computer_info :
        
        if each_value == 'A' :
            total_A += val_A
            
        elif each_value == 'B' :
            total_B += val_B
            
        elif each_value == 'C' :
            total_C += val_C
            
        elif each_value == 'D' :
            total_D += val_D
            
        elif each_value == 'E' :
            total_E += val_E
            
    # input new info
    info = input().split()
            
# 3 : index max value
name_component = ['A','B','C','D','E']
total_val = [total_A , total_B , total_C , total_D , total_E]

max_value = max(total_val)
pos_max = total_val.index(max_value)
print( name_component[pos_max] , max_value )

