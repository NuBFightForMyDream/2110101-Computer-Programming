# 1 : input info
info = []
line = int(input())
for i in range(line) : 
    inp = input()
    info += [inp]
    
# 2 : check algo
algo = input()

# case 1 : rotation 90 degree -> outer loop = len(inp)
    # ex : 3x4 (col 3 row 4) -> 4x3 (col 4 row 3)
    # outer loop = 4 = len(inp)
    # inner loop = element reverse (in info)
    # dont forget to reset str_out & print

if algo == 'rot90' :
    # define str_out
    str_out = ''
    for j in range(len(inp)) : # outer loop : row
        for ele in info[::-1] : # inner loop : column
            str_out += ele[j]
        # out of inner loop -> print & reset str
        print(str_out)
        str_out = ''
        
# case 2 : rotation 180 degree -> reverse inner & outer loop
elif algo == 'rot180' : 
    # reverse inner & outer
    info = info[::-1]
    # for loop -> print reverse
    for ele in info :
        print(ele[::-1])