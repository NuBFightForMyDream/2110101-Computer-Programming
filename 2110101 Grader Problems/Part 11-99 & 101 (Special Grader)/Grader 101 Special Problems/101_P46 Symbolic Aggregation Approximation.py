def SAX(x,k) :
    # x is list of time series , k is consecutive number
    
    ### Step 1 : create Z-score of list x
    
    # 1.1 : find mean of list
    mean = sum(x) / len(x)
    
    # 1.2 : find sd of list x
    sum_x_square = 0
    for xi in x : sum_x_square += (xi - mean) ** 2
    sd = (sum_x_square / len(x)) ** 0.5
    
    # 1.3 : calculate Z-score
    z = [(xi - mean)/sd  for xi in x]
    
    ### Step 2 : find mean of consecutive pair
    p = []
    for i in range(0 , int(len(z)/k) + 1 , 1) :
        # start with index 0,1,2,... until len(z)/k (+1 too)
        # then choose range of z for that slice divide by range of that slice
        mean_consecutive = sum(z[i*k : (i+1)*k : 1]) / len(z[i*k : (i+1)*k : 1])
        # add value to p
        p.append(mean_consecutive)
        
    ### Step 3 : transform p to alphabet -> check condition
    sax_info = ''
    for pj in p :
        if pj <= -0.84 : sax_info += 'a'
        elif -0.84 < pj <= -0.25 : sax_info += 'b'
        elif -0.25 < pj <= 0.25 : sax_info += 'c'
        elif 0.25 < pj <= 0.84 : sax_info += 'd'
        elif pj > 0.84 : sax_info += 'e'
    
    ### Step 4 : return string
    return sax_info

### Calling function for use (inout k,x)
k = int(input())
x = [float(e) for e in input().strip().split()]
print(SAX(x,k)) # print value
        