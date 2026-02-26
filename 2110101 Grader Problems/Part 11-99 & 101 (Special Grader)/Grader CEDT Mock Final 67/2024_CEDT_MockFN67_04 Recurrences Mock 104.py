# 1 : define 3 fns
import math

def S(n,k) : # Stirling Number of the Second Kind
    # S(0,0) = 1
    if n == 0 and k == 0 : return 1 
    # S(n,0) = S(0,n) = 0
    if (n == 0) or (k == 0) : return 0
    # general case -> S(n+1 , k) = kS(n,k) + S(n,k-1)
    # change n : S(n,k) = kS(n-1,k) + S(n-1,k-1)
    return k*S(n-1 , k) + S(n-1 , k-1)

def B(n) : # Bell Number
    # B(n+1) = k=0Σn[C(n,k) x B(k)]
    # change n+1 -> n : B(n) = k=0Σn-1[C(n-1,k) x B(k)]
    if n == 0 : return 1
    # general case
    B_value = 0
    for k in range(0 , n-1) :
        B_value += (math.factorial(n) / math.factorial(k) / math.factorial(n-k) * B(k)) # import math for combi.
    return B_value


    