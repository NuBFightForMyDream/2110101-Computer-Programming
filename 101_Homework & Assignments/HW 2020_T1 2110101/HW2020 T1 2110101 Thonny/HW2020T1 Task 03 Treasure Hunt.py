# 1 : define initial var (world , size , fn)

size = 10    # size of world N * N 
world = [[0]*size for i in range(size)] # world is nested list 
 
# bottomleft is (0,0), x goes right, y goes up 
def printworld():
    # reverse row for print (cuz row start from last row)
    
    '''
    for row in range(size-1,-1,-1):
        world_each_row = ''
        for col in range(size): 
            world_each_row += str(world[col][row]) + " " # join by using end = ' ' for each char
        print(world_each_row) 
    '''
        
## for nice effect (print each char)

    for i in range(size-1,-1,-1): 
        for j in range(size): 
            print(world[j][i], end = " ") 
        print()
      
# -----------------------------------------------------------------------

# 2 : define main structure of program (forward, turnleft , turnright , makemove , origin , test , joinmap , main)

# 2.1 : heading & turnhead

hd = 0   # heading 0-N, 1-E, 2-S, 3-W 
px = 0   # current position x 
py = 0   # current position y 
 
# move forward one step 
def forward(): 
    global hd, px, py 
    # move one step 
    if(hd == 0): 
        py += 1 
    elif(hd == 1): 
        px += 1 
    elif(hd == 2): 
        py -= 1 
    elif(hd == 3): 
        px -= 1 
    # constrain x,y in bound 0..N-1 
    if(px > size-1): 
        px = size-1 
    if(px < 0): 
        px = 0 
    if(py > size-1): 
        py = size-1 
    if(py < 0): 
        py = 0
    # mark pos. we've visited as 1
    world[px][py] = 1 
 
# turn head left 90 degree 
def turnleft(): 
    global hd 
    hd -= 1 
    if(hd < 0): # if heading is minus -> set heading to 3(W)
        hd = 3 
 
# turn head right 90 degree 
def turnright(): 
    global hd 
    hd = (hd + 1) % 4 # set heading to 0-3
 
# 2.2 : make move according to m (map) 
def makemove(m): 
    for c in m: 
        if(c == "F"): 
            forward() 
        elif(c == "L"): 
            turnleft() 
        elif(c == "R"): 
            turnright() 
 
# 2.3 : origin , test , joinmap
def origin(x,y): 
    global px,py 
    px = x 
    py = y 
    world[px][py] = 1 # mark visted as 1
  
# test structure of program
def test(): 
    origin(1,1) 
    mymap = "FFLRFRLL" # example of algorithms
    makemove(mymap) 
    printworld() 
     
def joinalgo(s1,s2): # joun algorithm of program
    s = s1 + s2
    return s 
 
# 2.4 : main function for program
def main(): 
    # 2.4.1 : set origin to (1,1) (start from bottomleft)
    origin(1,1) 
    s1 = str(input('Enter Algo #1 (Ex : FFRLLF) : ').strip()) # input algorithm #1 
    s2 = str(input('Enter Algo #2 (Ex : FFRR) : ').strip()) # input algorithm #2
    
    # 2.4.2 : join algorithm -> makemove -> get result (printworld)
    s = joinalgo(s1,s2) 
    makemove(s) # run algorithm
    printworld() # print result
     
# run main fn
test() 
 
# ------------------------end ----------------------------------------------- 