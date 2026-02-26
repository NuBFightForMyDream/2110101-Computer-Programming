# Prog-02: Beautiful Parametric Equation 
# 6730084521 Chatrphol Ovanonchai

# 1 : write LaTex equations (with $ ends)
# $ x(t)=2.5sin(-5t)^22^{(cos(cos(9.844t)))} $   
# $ y(t)=2.5sin(sin(-5t))cos(9.844t)^2$  

# This program generates Einstein Eqautions
# I've chosen this equation by myself. 
 
# 2 : import math & matplotlib
import math 
import matplotlib.pyplot as plt 

# ------------- 
# 3 : setting up period (T)
def setup_period(min_t, max_t, dt): 
    T = []; t = min_t
    while t <= max_t:              
        T.append(t) 
        t += dt 
    if t != max_t: T.append(max_t) 
    return T 
#------------------------------------ 
# 4 : plotting x,y points
def plot(x, y, min_t, max_t, dt): 
    T = setup_period(min_t, max_t, dt) 
    X = [x(t) for t in T]  
    Y = [y(t) for t in T] 
    plt.plot( X, Y, 'pink' ) 

# ==================================== 
# 5 : define x,y
def x(t): 
    xt = 2.5*math.sin(-5*t)**2 * 2**(math.cos(math.cos(9.844*t))) 
    return xt 
 
def y(t): 
    yt = 2.5*math.sin(math.sin(-5*t)) * math.cos(9.844*t)**2 
    return yt 
 
# 6 : call fn plot (x&y) & show graph
plt.title('Parametric Equations 6730084521')
plot(x, y, -6, 6, 0.01) # called setup_period inside already
plt.show() 