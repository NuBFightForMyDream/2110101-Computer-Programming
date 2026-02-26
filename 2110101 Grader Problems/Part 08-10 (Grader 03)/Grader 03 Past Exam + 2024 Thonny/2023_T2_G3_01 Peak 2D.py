# 1 : create 2 fns

# fn1 : read data
def read_data() :
    dat = [] # for append list of list
    R = int(input()) # nb.of rows
    for r in range(R) :
        dat.append( [int(e) for e in input().strip().split()] ) # append list comp
        # out of loop -> return data
    return dat
     
# fn2 : count peaks (higher than corners)
def count_peak(data) :
    # consider only row 1 to second last row [1:-1] , likewise col [1:-1]
    # check peak : Ex : consider[11] -> check [10],[01] -> row-1 & col-1
    count = 0
    for row in range(1 , len(data)-1) : # consider (R-1)x(C-1)
        for col in range(1 , len(data)-1) :
            if (data[row][col] > data[row-1][col]) and (data[row][col] > data[row+1][col]) and  \
               (data[row][col] > data[row][col-1]) and (data[row][col] > data[row][col+1]) :
                   # top-bottom & left-right
                count += 1
    return count

exec(input().strip())