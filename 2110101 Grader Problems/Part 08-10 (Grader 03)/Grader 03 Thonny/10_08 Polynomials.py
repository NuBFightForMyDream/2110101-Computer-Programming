def add_poly(p1 , p2) :
    # using tuple makes ur life 100x harder -> using dict maybe easier
    p_add = {}
    
    # 1 : for loop p1 first -> add key:value to dict
    for (cof1 , pol1) in p1 :
        p_add[pol1] = cof1 # key = pol , value = cof
        
    # 2 : for loop p2 -> check if element already in dict
    for (cof2 , pol2) in p2 :
        if pol2 not in p_add :
            p_add[pol2] = cof2
        else :
            p_add[pol2] += cof2 # add val to val in p_add
    
    # 3 : now we got dict -> we'll sort & append to list of tuple    
    addlist = []
    
    # 3.1 : append val:key 
    for key in p_add : # key = pol
        if p_add[key] != 0 : # append key:val if cof != 0
            addlist.append( (key , p_add[key]) )
            
    # 3.2 : sort reverse & reverse element
    addlist = sorted(addlist , reverse = True)
    for i in range(len(addlist)) :
        addlist[i] = addlist[i][::-1]

    # 3.3 : return dict
    return addlist
      
# execute input
for i in range(3) : 
    exec(input())
    