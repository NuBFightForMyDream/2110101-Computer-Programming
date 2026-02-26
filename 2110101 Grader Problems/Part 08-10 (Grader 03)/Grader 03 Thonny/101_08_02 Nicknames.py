# 1 : enter loop & add each key , value in dict
loop_name = int(input('Enter Loop : '))
dict_name = {}
for i in range(loop_name) :
    key , value = input('Enter Name , Nickname : ').split()
    dict_name.update({key : value})
    
# check key in dict

reverse_dict = { value:key for key,value in dict_name.items() }

loop_check = int(input('Enter Loop : '))
for i in range(loop_check) :
    check = input('Check Nickname Or Name : ')
    
    if (check in dict_name.keys()) :
        print(dict_name[check])
        
    elif (check in dict_name.values()) :
        # swap key & value -> check new key    
        print(reverse_dict[key])   
    else :
        print('Not found')

