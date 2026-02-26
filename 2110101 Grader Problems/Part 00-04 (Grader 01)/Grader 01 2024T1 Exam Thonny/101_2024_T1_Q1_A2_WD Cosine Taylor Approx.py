# 1 : input x,e & import math
import math
x,e = [float(e) for e in input().split()]
sum_cosine = 0

# 2 : calculate first term before while loop
n = 0 # for exponential fn
cosine_term = ((-1)**n) * (x**(2*n)) / math.factorial(2*n) # for finding present term

# 3 : while loop
while abs(cosine_term) > e :
    # process in this loop : sum -> +n -> cosine
    # calculate last for checking if still in loop
    
    # sum to cosine
    sum_cosine += cosine_term
    # add loop
    n += 1
    # calculate cosine first
    cosine_term = ((-1)**n) * (x**(2*n)) / math.factorial(2*n)

# 4 : print & round 
print( round(sum_cosine , 6) )