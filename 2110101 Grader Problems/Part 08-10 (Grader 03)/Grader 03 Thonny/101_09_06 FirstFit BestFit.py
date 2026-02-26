# define 4 fns
def first_fit(L , e) :
    # put e in first sublist that can fit (cd : <= 100)
    # if can't fit any element -> add new value instead
    
    # case 1 : can fit
    # check each element -> check if sum then <= 100
    for ele in L :
        if sum(ele) + e <= 100 :
            ele.append(e)
            return L # return immediately
    
    # case 2 : can't fit -> append new sublist
    return L.append([e])

def best_fit(L , e) :
    # put e in sublist that nearest to 100 (cd : <= 100)
    # if can't fit any element -> add new value instead

    # define list comp. for nearest 100
    dist = [ 100-sum(ele)+e for ele in L ]
    check = []
    for ele in dist :
        if ele < 100 : check.append(True)
        else : check.append(False)
    
    # case 1 : can fit -> check cd. then append
    for i in range(len(dist)) :
        # check if that element is nearest 100
        if dist[i] == max(dist) and check[i] == True : 
            L[i].append(e)
            return L # return immediately
       
    # case 2 : can't fit -> append new sublist
    return L.append([e])

exec(input().strip())