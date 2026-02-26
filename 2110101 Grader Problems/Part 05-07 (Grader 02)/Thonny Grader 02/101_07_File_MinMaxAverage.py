# 1 : input filename , year
filename , year = input().split()

# 2 : open & close file

# 2.1 : open file
nisit_info = open(filename , 'r') # open and read file

# define list (for storing nisit info)
stu_ids = [] # keep only student in that academic yr
points = [] # keep only student in that academic yr
found_data = False # for checking if nisit info in list

# 2.2 : read every line (use for loop)
for line in nisit_info :
    
    # now = inside file -> check year & find pts
    stu_id , point = line.split()
    
    if year[2:] == stu_id[0:2] : # consider 6x and 6x nisit_id
        stu_ids += [ stu_id ]
        found_data = True
        points += [ float(point) ] # convert point to float
        
# out of for loop -> find avg , max , min
if found_data == True : 
    max_point = max(points)
    min_point = min(points)
    average = sum(points) / len(points)
    # print min , max , avg
    print(min_point , max_point , average)

if found_data == False :
    print('No data')
    
# close file
nisit_info.close()