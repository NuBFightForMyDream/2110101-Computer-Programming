# Key : create trendline for coordinate input

# 1 : input info + define initial var. (see from equation)
xi = [float(e) for e in input().split()]
yi = [float(e) for e in input().split()]

sum_xy = 0
sum_x = 0 ; sum_y = 0
sum_x_square = 0
N = len(xi) # = len(yi) = number of coordinates

# 2 : for loop (using 'for element in list' cmd)
for point in range(N) :
    # can use len(yi) too because len(xi) = len(yi)
    
    # now , we'll sum each coordinate to var.
    sum_xy += xi[point] * yi[point]
    
    sum_x += xi[point]
    sum_y += yi[point]
    
    sum_x_square += (xi[point] ** 2)
    
# 3 : calculate slope and intercept
delta_y = N*(sum_xy) - (sum_x)*(sum_y)
delta_x = N*(sum_x_square) - (sum_x)**2

slope = delta_y / delta_x # same value as m

y_intercept = ((sum_y) - slope*(sum_x)) / N # same value as b

# 4 : check algorithm (input algorithm first)
algorithm = input().strip()

if algorithm == 'mb' : # find m & b
    print( round(slope , 3) , round(y_intercept , 3) )
    
elif algorithm == 'func' : # func
    # check slope : >1/<-1 (general) , 0 , 1 , -1
    if slope == 1 :
        # check y-intercept >0 , 0 , <0
        if y_intercept > 0 : 
            print(f'y = x + {abs(round(y_intercept , 3))}')
        elif y_intercept < 0 :
            print(f'y = x - {abs(round(y_intercept , 3))}')
        else : # y_intercept = 0
            print(f'y = x')
            
    elif slope == 0 :
        # check y-intercept >0 , 0 , <0
        if y_intercept > 0 : 
            print(f'y = {abs(round(y_intercept , 3))}')
        elif y_intercept < 0 :
            print(f'y = - {abs(round(y_intercept , 3))}')
        else : # y_intercept = 0
            print(f'y = 0')
            
    elif slope == -1 :
        # check y-intercept >0 , 0 , <0
        if y_intercept > 0 : 
            print(f'y = -x + {abs(round(y_intercept , 3))}')
        elif y_intercept < 0 :
            print(f'y = -x - {abs(round(y_intercept , 3))}')
        else : # y_intercept = 0
            print(f'y = -x')
    
    else : # slope > 1 , slope < -1
        # check y-intercept >0 , 0 , <0
        if y_intercept > 0 : 
            print(f'y = {round(slope , 3)}x + {abs(round(y_intercept , 3))}')
        elif y_intercept < 0 :
            print(f'y = {round(slope , 3)}x - {abs(round(y_intercept , 3))}')
        else : # y_intercept = 0
            print(f'y = {round(slope , 3)}x')
            
