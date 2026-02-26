# 1 : input x & epsilon (threshold)
import math
x , epsilon = [float(e) for e in input().split()]

# 2 : calculate value -> check if still in while loop
sum_sinh = 0 ; n = 0 # given initial value

sinh_x = ( x**(2*n + 1) ) / math.factorial(2*n + 1)

while abs(sinh_x) > epsilon : # still more than threshold
    # add to sum_sinh
    sum_sinh += sinh_x
    # increment n by 1
    n += 1
    # calculate new sinh value
    sinh_x = ( x**(2*n + 1) ) / math.factorial(2*n + 1)
    
# round final result 6 decimal pts
print( round(sum_sinh , 6) )