#
# 2567_3_Q1_A2: 2567_3_Q1_A2: Boy Scout 
#

# 1 : input info
info_scout = input().split() # scouts info (list)
cut_num = int(input()) # cout to this number , will cut and arrange new row

color_scout = [] # will stores scout's color (like dict)
all_colors = [] # stores color name

color_name = input().split()
while len(color_name) == 1 : # assuming that we want to find 2++ scout's color
    all_colors += color_name
    # input next info
    color_name = input().split()
    
# define last color_name to find_list
find_list = color_name

# ----------------------------------------------------
# 2 : arrange scout
pos_color = 0 # pos for colors

for pos in range(len(info_scout)) : # start counting at 1
    # check if cut?
    if pos % cut_num == 0 and pos != 0 :
        # cut to new line
        pos_color += 1 # add pos 1

    color_scout += [ all_colors[pos_color] ]
    
# ----------------------------------------------------
# 3 : find color
out_color = ""
for name_scout in find_list :
    # while loop : find if found same name as element
    pos_found_name = 0
    while pos_found_name < len(color_scout) :
        if name_scout == info_scout[pos_found_name] :
            break # got pos_found_name
        else :
            pos_found_name += 1
        
    # add str to output (index color_scout)
    out_color += color_scout[pos_found_name] + ' '
    
print(out_color)