# define class Point (for coordinates (x,y) )
class Point :
    # annouce var. in init fn
    def __init__(self , x, y) :
        self.x = x
        self.y = y
    # define str magic method
    def __str__(self) :
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    
# define class Rect (checking area & point in rect)
class Rect :
    # annouce var. in initial fn
    def __init__(self , p1 , p2): # p1 ,p2 = object
        self.lowerleft = p1
        self.upperright = p2
        
    # define area method
    def area (self) :
        ### Note : calling x,y inside Point class
        # self.lowerleft = Point(x1 , y1) 
        # self.upperright = Point(x2 , y2)
        
        # define dx,dy then return area (dx * dy)
        dx = self.upperright.x - self.lowerleft.x
        dy = self.upperright.y - self.lowerleft.y
        return dx * dy
    
    # define contains method
    def contains(self , p) : # checking if p (point) in rect
        # checking value in x-axis and y-axis
        cd_x = self.lowerleft.x <= p.x <= self.upperright.x # bool
        cd_y = self.lowerleft.y <= p.y <= self.upperright.y
        
        # check if both cd are true
        if (cd_x == True) and (cd_y == True) : return True
        return False # else not in rect
    
# --------- Input Zone -------------------------------------------

# 1 : input info
x1, y1 , x2 , y2 = [int(e) for e in input().split()]

# 2 : define object
lowerleft = Point(x1 , y1)
upperright = Point(x2 , y2)

# 3 : call Rect class
rect = Rect(lowerleft , upperright) # rect = var. of object
print(rect.area()) # call area method

# 4 : input info & call contains fn (inside Rect class)
m = int(input())
for i in range(m) :
    x,y = [int(e) for e in input().split()]
    p = Point(x,y)
    print(rect.contains(p))