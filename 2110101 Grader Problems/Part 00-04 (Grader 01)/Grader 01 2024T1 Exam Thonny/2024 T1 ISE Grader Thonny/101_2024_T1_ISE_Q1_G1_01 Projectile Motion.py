# 1 : input v0 , theta
# theta is measured by floor
import math

# check nb of input first
info = input().strip().split()

if len(info) != 2 :
    print('Error!')
    
else :
    # check info
    v0 , theta_deg = float(info[0]) , float(info[1])

    # 2 : calculate formula
    theta_rad = math.radians(theta_deg)
    g = 9.81 # acceleration

    # 2.1 : maximum height -> vy^2 / 2g
    h_max = abs( (v0**2) * (math.sin(theta_rad))**2 / (2*g) )

    # 2.2 : maximum range -> vx * t (t = 2vsin/g)
    range_max = abs( (v0**2) * math.sin(2 * theta_rad) / g )

    # 2.3 : time of flight
    time_to_floor = abs( (2 * v0 * math.sin(theta_rad)) / g )

    # 3: print output -> check error
    print(f"{h_max:.2f} {range_max:.2f} {time_to_floor:.2f}")
