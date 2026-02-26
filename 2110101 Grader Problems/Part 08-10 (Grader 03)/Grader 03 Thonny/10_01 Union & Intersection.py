# 1 : input loop -> enter info
info = [] # create empty set first
for i in range( int(input()) ) :
    # 1.1 : add set comp.
    num = {int(e) for e in input().split()}
    # 1.2 : add subset into list
    info.append(num) # list (of set)
    
# 2 : for loop each element in set

# check input first if not vacant
if info == [] : # loop = 0 -> no append
    union = intersect = set() # define as empty set
    
else : # normal case     
    # 2.1 : set starting set first
    union = info[0]
    intersect = info[0]
    
    # 2.2 : for loop -> Union & Intersect until last char
    for i in range(1 , len(info)) : # start at index 1 (id0 is starting set)
        # replace new value in old var.
        union = union | info[i]
        intersect = intersect & info[i]
    
# 3 : in every case -> print length
print(len(union))
print(len(intersect))
    
