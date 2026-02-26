# import numpy first
import numpy as np

# define fn
def read_data() : # receive input -> return 2 array (weight , data)
    # input info into w list
    w = [float(e) for e in input().split()]
    # create weight array from list w
    weight = np.array(w)
    # input info -> keep in data array
    n = int(input())
    data = np.ndarray( (n,4) , int ) # shape 2D nx4
    for i in range(n) :
        data[i] = [int(e) for e in input().split()] # replace each index
    # out of loop
    return weight , data
    # weight = 1D Array , data = 2D array
    
def report_lower_than_mean(weight , data) :
    # data array col : sid , midterm , project , final
    
    # 1 : create ndarray for storing total score
    total_score = np.ndarray( (data.shape[0]) , int ) # 1D : len = row(data)
    
    # 2 : calcuate score -> store in array (slice first)
    score = data[ : , 1: ]# score = nx3 array (2D)
    
    # 3 : dot array (2D begin frist)
    total_score = np.dot(score , weight) # 2D (5x3) dot 1D (3) => total_score = 1D (5)

    # 4 : create 1D array (stu_ids) for checking if someone is lower tahn mean (choose index only True)
    stu_ids = data[ : , 0].T # 2D -> 5x1 -> Transpose 1x5
        # choose only True ids
    lower_check = (total_score < np.mean(total_score)) # check bool first
    lower_ids = stu_ids[lower_check] # need only True
    
    # 5 : check length of array
    if lower_ids.shape[0] > 0 : # len > 0
        print(', '.join([str(e) for e in lower_ids])) # change to list of str -> join
        
    else : # No stuent -> return None
        print('None')

# execute input
exec(input())