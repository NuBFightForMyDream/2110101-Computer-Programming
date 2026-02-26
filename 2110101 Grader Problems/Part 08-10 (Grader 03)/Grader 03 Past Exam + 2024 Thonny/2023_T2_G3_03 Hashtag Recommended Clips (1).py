# 1 : input info & store in dict
info_clip = {}

info = input().split()
while info != ['q'] :
    name = info[0] ; hashtags = info[1:] # name = str , hashtags = list
    # add key:val to dict 
    info_clip[name] = hashtags
    # still input
    info = input().split()
    
# 2 : input info then check val in dict
watch = input().split() # clip01 , ...

# 2.1 : create list of list for storing most recommended clips
most_rec = [] # list

# 2.2 : outer loop -> check value (hashtags) from dict (clipname)
for name in watch : # name = clip01
    # inner loop -> check count & store in list (of list)
    for ele in info_clip[name] :
        count_hash = 0
        for key in info_clip :
            count_hash += info_clip[key].count(ele) # val.count(ele)
        
        most_rec.append([ele , count_hash])
            