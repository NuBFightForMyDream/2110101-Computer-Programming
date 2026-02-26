# 1 : input loop
nb_line = int(input())
list_code = []

# 2 : input & store in list_code
for i in range(nb_line) :
    code = input().strip()
    # add space at ending (in case code is '')
    list_code.append(code + ' ')

# 3 : check element
for i in range(len(list_code)) :
    
    # 3.1 : check if first letter is '.'
    if list_code[i][0] == '.' :
        # 3.1.1 : set count to 0 (count for .)
        count = 0
        # 3.1.2 : check each char in each element in list_code
        for j in range(len(list_code[i])) :
            if list_code[i][j] == '.' :
                count += 1
            else : # if found alphabet -> break
                break
        # break -> got count (out of for loop)
        print('.' * int(count/2) + list_code[i][j:])
        # j = new value (that found char.) -> start print with index j
        
    # 3.2 : if first letter is not '.' -> print them
    else :
        print(list_code[i])
