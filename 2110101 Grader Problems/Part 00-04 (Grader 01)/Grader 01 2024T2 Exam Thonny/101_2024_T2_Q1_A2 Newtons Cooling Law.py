# 1 : input info
old_temp = float(input())
room_temp = float(input())
time_interval = float(input())
material_type = int(input())
wind_velocity = int(input())

# 2 : set initial value 
    # 2.1 : create delta_temp for using loop
new_temp = room_temp
delta_temp = abs(old_temp - room_temp)
    # 2.2 : update time_passed
time_passed = 0
    # 2.3 : create list of material type & wind velocity
        # we give index 0 for user input (start at 1)
        # then calculate for k_total = k_mat * k_win
k_materials = [0 , 0.05 , 0.02 , 0.01 , 0.015]
k_wind = [0 , 1.5 , 1 , 0.8]
k = k_materials[material_type] * k_wind[wind_velocity]

# 3 : while loop -> calculate temp. & time
while delta_temp > 1e-3 :

    # 3.1 : calculate new_temp using new formula
    new_temp = old_temp - k*(old_temp - room_temp)*time_interval
    
    # 3.2 : update time passed
    time_passed += time_interval
    
    # 3.3 : update delta temp
    delta_temp = abs(old_temp - new_temp)
    
    # 3.4 : update last temp for next loop
    old_temp = new_temp # old_temp value are from previous calculation
   
# 4 : check if not in loop -> add time_interval to time_passed
if time_passed == 0 :
    time_passed += time_interval
   
# 5 : print output
print( round(time_passed,2) , round(old_temp,3) ) # can use new_temp too cuz its equal (before next loop)