# 1 : input loop & str
old_str = []
loop = int(input()) # Enter number of line

for i in range(loop) :
    str_in = input() # Enter String
    old_str += [ str_in ]
    
# 2 : end loop -> use old_str list for changing elements inside
algo = input()

if algo == 'hflip' :
    # swap element in side , no swap pos.
    for i in range(loop) :
        old_str[i] = old_str[i][::-1] # reverse char in each element
        print(old_str[i])

elif algo == 'vflip' :
    # swap pos. only , no swap elements inside
    new_str = old_str[::-1]
    for i in range(len(new_str)) :
        print(new_str[i])
    
