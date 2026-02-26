# 1 : input info & store in bnk dict
info = input()
bnk = dict() # for storing info

while len(info) != 1 :
    # split info
    fan , idol , vote = info.split(); vote = int(vote)
    # check if having fan in dict
    
    # case 1 : fan in dict -> check if idol in dict (in value)
    if fan in bnk :
        # 1.1 : idol in valdict -> plus vote
        if idol in bnk[fan] :
            bnk[fan][idol] += int(vote)
        # 1.2 : idol not in valdict -> update new subdict in valdict
        else :
            bnk[fan].update({idol:vote})
            
    # case 2 : fan not in dict -> add new key:val to dict
    else :
        bnk[fan] = {idol: vote}
        
    # still input info
    info = input()
    
# 2 : define fn -> calculate each algorithm
def ranked_by_total_score(bnk) : # bnk = dict
    # define dict -> calculate each key in dict
    top_votes = dict()
    
    # for loop each key & each subkey
    for each_fan in bnk :
        # for loop each subkey in subdict
        for each_idol in bnk[each_fan] :
            # check if have that info in top_votes already
            if each_idol in top_votes :
                top_votes[each_idol] += bnk[each_fan][each_idol] # = votes
            else : # key not in top_votes
                top_votes[each_idol] = bnk[each_fan][each_idol] # = votes 
                
    # sort value descending (no need to care alphabetical)
    ranked = sorted([[v,k] for k,v in top_votes.items()] , reverse = True)
    # return ranked
    return ranked

def ranked_by_people_voted(bnk) :
    # define dict -> calculate each key in dict
    idol_votes_info = dict()
    
    # logic : key = idol , val = list of fans
    for each_fan in bnk :
        # for loop each subkey in subdict
        for each_idol in bnk[each_fan] :
            # check if have that info in top_votes
            if each_idol in idol_votes_info :
                idol_votes_info[each_idol].append(each_fan)
            else :
                idol_votes_info[each_idol] = [each_fan] # if fan,idol same as before -> replace itself
    # sort dict
    ranked = sorted([[len(v),k] for k,v in idol_votes_info.items()] , reverse = True) # change list(val) to int(len)
    # return list
    return ranked

def ranked_by_kamioshi(bnk) :
    # define dict -> calculate each key in dict
    kamioshi_info = dict()
    
    # logic : key = fan , val = kamioshi

    # 1 : get kamioshi of each fan
    for each_fan in bnk :
        # sort value by alphabetical first -> sorted then dict
        bnk[each_fan] = dict(sorted(bnk[each_fan].items()))
        # get key that have max value
        kamioshi_info[each_fan] = max(bnk[each_fan] , key = bnk[each_fan].get) # bnk[each_fan] = idol votes
            
    # 2 : for loop -> count votes
    kamioshi_votes = dict()
    for each_fan in kamioshi_info :
        if kamioshi_info[each_fan] in kamioshi_votes : # kamioshi_info[each_fan] = idol
            # idol in max_votes -> +1
            kamioshi_votes[ kamioshi_info[each_fan] ] += 1
        else : # idol not in max_votes -> add new key:val
            kamioshi_votes[ kamioshi_info[each_fan] ] = 1
            
    # sort dict
    ranked = sorted([[v,k] for k,v in kamioshi_votes.items()] , reverse = True) # change list(val) to int(len)
    # return list
    return ranked

# 3 : join str -> check case that input
if info == '1' : 
    top3_list = ranked_by_total_score(bnk)
elif info == '2' :
    top3_list = ranked_by_people_voted(bnk)
elif info == '3' :
    top3_list = ranked_by_kamioshi(bnk)
    
# sort str
top3_str = ''
for i in range(3) :
    top3_str += (top3_list[i][1]) + ', '
print(top3_str.strip(', '))

     