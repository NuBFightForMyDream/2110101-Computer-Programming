def reverse(d) : # d = dict
    # swap key & value -> for loop in items
    reverse_dict = {}
    for key , value in d.items() :
        key , value = value , key # swap values
        reverse_dict.update({key : value}) # update element in new dict
    # return reverse_dict
    return reverse_dict
        
def keys(d,v) : # d = dict , v = value
    # check value -> if v = value -> update key into list
    list_add = [] # create vacant list
    for key in d : # for loop -> check key
        if d[key] == v :
            # d[key] = value -> check if each value in dict = v
            list_add += [key] # add key into lisst
    # end loop -> return list
    return list_add

# execute fn
exec(input().strip())