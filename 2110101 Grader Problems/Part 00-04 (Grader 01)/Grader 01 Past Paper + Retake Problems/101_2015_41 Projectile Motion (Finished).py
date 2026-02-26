# Key : หาตัวเเปรอื่นๆ ของการคิดการเคลื่อนที่ projectile

# 1 : รับ input v0 , theta เข้ามา
v0 = float(input('Enter Initial Velocity (m/s) : ')) # float
theta_deg = float(input('Enter Horizonal Angle (deg) : ')) # float

# 2 : import math + แปลงค่า theta ก่อน เผื่อนำไปใช้
import math
theta_rad = theta_deg * (2*math.pi / 360) # เเปลงเเล้ว นำไปเข้า math.sin/cos ได้
g = 9.81 # gravity acceleration (free fall) -> m/s^2

# 3 : เข้าสูตร projectile หา t (พื้น->พื้น) , Sx , Sy (สูตรฟิสิกส์ลองไปนั่งprove ดู)

# 3.1 : หา t_floor ก่อน
time_max = v0 * math.sin(theta_rad) / g # floor -> max
time_floor = 2 * time_max # floor -> max -> floor

# 3.2 : หา Sx_max = Vx * t
vx = v0 * math.cos(theta_rad) # Vx
x_max = vx * time_floor # Sx max = Vx * t_floor

# 3.3 : หา Sy => suvat (ใช้ time_max)
vy = v0 * math.sin(theta_rad) # Vy
y_max = (vy * time_max) + (1/2 * -g * (time_max)**2)

# 4 : print Sx_max , Sy_max 3 ตน.
print('Maximum distance (x) : %.3f' %x_max) # m
print('Maximum height (y) : %.3f' %y_max) # m
