# 1 : input cmd
bas_cmd = input().strip()
pos = 0

# create var. for basketball
home_success = 0 ; home_totalshoot = 0 ; home_points = 0
visiting_success = 0 ; visiting_totalshoot = 0 ; visiting_points = 0

# 3 : check if still in loop
while pos < len(bas_cmd) :
    
    if bas_cmd[pos] == 'H' :
        home_success += 1
        home_totalshoot += 1
        home_points += int(bas_cmd[pos + 1])
        pos += 2
        
    elif bas_cmd[pos] == 'h' :
        home_totalshoot += 1
        pos += 1
        
    elif bas_cmd[pos] == 'V' :
        visiting_success += 1
        visiting_totalshoot += 1
        visiting_points += int(bas_cmd[pos + 1])
        pos += 2 # +2 for next cmd
        
    elif bas_cmd[pos] == 'v' :
        visiting_totalshoot += 1
        pos += 1  #+1 for next cmd
    
# 4 : calculate rate (if 0 -> given as 0.0)
home_rate = (home_success / home_totalshoot * 100) if home_totalshoot > 0 else 0.0
visiting_rate = (visiting_success / visiting_totalshoot * 100) if visiting_totalshoot > 0 else 0.0

# 5 : print result
print('H =' , home_points , '%H =' , round(home_rate , 2) )
print('V =' , visiting_points , '%V =' , round(visiting_rate , 2) )