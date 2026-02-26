# 1 : import math & input
import math
theta_deg1 , theta_deg2 , radius = [float(e) for e in input().split()]

# 2 : calculate formula

# 2.1 : convert angle to radian first
theta_rad1 = math.radians( theta_deg1 )
theta_rad2 = math.radians( theta_deg2 )

# 2.2 : define formula -> results are positive -> abs value
distance = abs( 2 * radius * math.sin( 0.5 * (theta_rad1 - theta_rad2)) )
area = (1/2) * abs(theta_rad1 - theta_rad2) * (radius**2)

# 3 : print value : fstring using {xxx:.4f} format
print(f"{distance:.4f} {area:.4f}")