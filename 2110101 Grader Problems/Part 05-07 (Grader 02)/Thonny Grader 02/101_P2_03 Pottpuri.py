# 1 : create 4 fns
def convex_polygon_area(p) : # parameter = p , return area (float)
    # p is list (of list)
    
    # 1 : add first element for completing cycle (change parameter)
    p += [ p[0] ] # add element for calculating polygon
    
    # 2 : find determinant
    det_plus = 0 ; det_minus = 0 # define det first
    
    for i in range(len(p) - 1) :
        det_plus += (p[i][0] * p[i+1][1]) # x_n * y_n+1
        det_minus += (p[i+1][0] * p[i][1]) # x_n+1 * y_n
        
    # out of loop -> calculate area
    area = abs(0.5 * (det_plus - det_minus))
    return area # float
        
def is_heterogram(s) : # check if string is repeated
    # 1 : change back to lower for safe + define bool (check_same)
    s.split()
    str_s = '' ; list_alphabet = []
    for i in range(len(s)) : # add lower string (no strange symbol)
        if s[i] not in ' \'[]"<>.,!@#$%^&*()\\/' :
            str_s += s.lower()[i]
    
    # 2 : for loop & check if that ele in string
    for i in range(len(str_s)) :
        if str_s[i] not in list_alphabet : 
            list_alphabet += [ s.lower()[i] ]
        elif str_s[i] in list_alphabet : # if 
            return False
    # if not in list -> no repeated char -> return True
    return True
    
def replace_ignorecase(s,a,b) :
    # s = string , a = want to change , b = changing word
    # Logic : check word in string
        # for loop -> can't use becuase we cant change i
        # while loop -> check until last char
            # if found a -> add b & skip
            # else => add nortmal char
            
    # define new string for output
    str_out = ''
    # define loop 
    i = 0
    while i < (len(s)) : # check until last char
        # if same char (lower) -> add b & skip loop 
        if s[i : i+len(a)].lower() == a.lower() :
            str_out += b
            i += len(a)
        # else -> add normal char    
        else :
            str_out += s[i]
            i += 1
    # return str_out
    return str_out

def top3(votes) :
    # 1 : create list_top3 first (for adding key into list)
    list_top3 = []
    # 2 : sort (.items()) (will give list) then dict() -> will give dict
    votes = dict(sorted(votes.items()))
    # 3 : for loop 3 times -> we need 3 element
    for i in range(3) : 
        # 4 : find key -> using max(dict , key = dict.get())
        top_key = max(votes , key = votes.get) # get key from dict with using max fn
        # 5 : add key into list
        list_top3 += [top_key]
        # 6 : give max value to 0 -> for next compare
        votes[top_key] = 0
    # 7 : out of loop -> return list
    return list_top3

# execute fn
for k in range(2):    
    exec(input())