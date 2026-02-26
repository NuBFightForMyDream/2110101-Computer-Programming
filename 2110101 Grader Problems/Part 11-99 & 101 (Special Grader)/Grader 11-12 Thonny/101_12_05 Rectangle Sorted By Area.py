# define class

# 1 : class Point -> read coordinates & store in str
class Point :
    # initial fn -> annouce var
    def __init__ (self , x , y) :
        self.x = x
        self.y = y
    # str magic method -> return str
    def __str__ (self) :
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    
# 2 : class Rect -> return str & sort area
class Rect :
    # initial fn -> annouce var
    def __init__ (self , p1 , p2) :
        # p1 , p2 = object -> call class Rect
        self.lowerleft  = p1
        self.upperright = p2
        
    # str magic method -> return str
    def __str__(self) : # no need to () again
        return str(self.lowerleft) + '-' + str(self.upperright)
    
    # define area fn (method) -> calculate area
    def area(self) : # self = p1 , p = p2
        dx = self.upperright.x - self.lowerleft.x # p2.x - p1.x
        dy = self.upperright.y - self.lowerleft.y # p2.y - p1.y
        return dx * dy
    
    # define lt magic method -> check if area1 (obj Rect1) < area2 (obj Rect2)
    def __lt__(self , rhs) :
        # calling fns in method by cmd : object.fn_name()
        return self.area() < rhs.area() # compare value
    
# -----------------------------------------------------------
# 1 : input info 
n = int(input())
rects = [] # list of object
for i in range(n):
    x1,y1,x2,y2 = [int(e) for e in input().split()]
    rects.append(Rect(Point(x1,y1), Point(x2,y2))) # append class Rect

# 2 : sort list
rects.sort()

# 3 : print each info
for i in range(n):
    print(rects[i])      