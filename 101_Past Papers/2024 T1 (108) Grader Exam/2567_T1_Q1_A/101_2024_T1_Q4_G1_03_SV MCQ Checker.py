# 1 : input info
info_solution = input().strip()
point_true , point_false = [int(e) for e in input().strip().split()]
info_nisit = input().strip()

# 2 : define var. for #nb. of choice T/F
choice_true = 0
choice_false = 0
choice_undefined = 0
total_point = 0

# 3 : check each char
for i in range(len(info_nisit)) :
    
    # case 1 : same answer
    if info_nisit[i] == info_solution[i] :
        # add choice_true , total_point
        choice_true += 1
        total_point += point_true
    
    # case 2 : not same answer -> check undefined
    else :
        # 2.1 : solution is 'X' -> check stu answer
        if info_solution[i] == 'X' : # add points automatically
            
            if (info_nisit[i] != '-') : # count true only
                choice_true += 1
                total_point += point_true
            
            elif (info_nisit[i] == '-') : # count true & undefined
                choice_true += 1
                choice_undefined += 1
                total_point += point_true                
            
        # 2.2 : solution is not 'X' , nisit answer is not '-'
        elif info_solution[i] != 'X' :
            
            if (info_nisit[i] != '-') : # count false
                choice_false += 1
                total_point += point_false
                
            elif (info_nisit[i] == '-') : # count undefined
                choice_undefined += 1
                # no need to add to total_points    
            
# check total_point if less than 0
if total_point < 0 : total_point = 0

# print info : true , false , undefined , total
print(choice_true , choice_false , choice_undefined , total_point)
    