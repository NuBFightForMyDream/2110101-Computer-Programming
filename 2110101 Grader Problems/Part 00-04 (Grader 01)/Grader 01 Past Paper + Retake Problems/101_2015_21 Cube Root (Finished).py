# 1 : รับ input a,b,c,d -> รับติดกัน ใช้ list comprehension
a,b,c,d = [int(e) for e in input('Enter A,B,C,D : ').split()] #int

# 2 : เเทนค่าทีละก้อน = import math
import math

# 2.1 : ให้ ด้านใน 2√ เป็น a1 , a2
a1 = ( (2*(b**3) - 9*a*b*c + 27*(a**2)*d )**2 - 4*(b**2 - 3*a*c)**3)
a2 = ( (2*(b**3) - 9*a*b*c + 27*(a**2)*d )**2 - 4*(b**2 - 3*a*c)**3)

# 2.2 : ให้ ด้านใน 3√ เป็น b1 , b2
b1 = (1/2) * ( 2*(b**3) - 9*a*b*c + 27*(a**2)*d + math.sqrt(a1))
b2 = (1/2) * ( 2*(b**3) - 9*a*b*c + 27*(a**2)*d - math.sqrt(a2))

# 2.3 : ให้ นอกสุด เป็น c1 , c2
c1 = (-b/(3*a)) - ( (1/(3*a)) * (b1)**(1/3) )
c2 = (-1/(3*a)) * ( b2 ** (1/3) )

# 2.4 : รวมค่า (มองดีๆ จริงๆคือก้อนเดียวกัน เเต่เขียนเเยกบรรทัด)
c_total = c1 + c2

# 3 : print cubic root ans
print('Value of Cubic Root : ' , c_total)