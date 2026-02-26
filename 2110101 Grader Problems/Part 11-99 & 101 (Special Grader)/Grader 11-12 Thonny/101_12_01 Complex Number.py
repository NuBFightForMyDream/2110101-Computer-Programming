# define class
class Complex :
    # 1 : define initial fn
    def __init__(self , a , b) :
        # a = Re , b = Im
        self.real = a
        self.imag = b
        
    # 2 : define str method
    def __str__(self) : # magic method => check case +1i , 0i , -1i
        
        # case 1 : real = 0
        if self.real == 0 :
            # case 1.1 : imag > 0 , case 1.2 : imag = 0 , case 1.3 : imag < 0
            if self.imag > 0 :
                if self.imag == 1 : return 'i'
                else : return str(self.imag) + 'i'
        
            elif self.imag == 0 : return str('0')
        
            else :
                if self.imag == -1 : return '-' + 'i'
                else : return '-' + str(abs(self.imag)) + 'i'
        
        # case 2 : real != 0
        if self.real != 0 :
            # case 1.1 : imag > 0 , case 1.2 : imag = 0 , case 1.3 : imag < 0
            if self.imag > 0 :
                if self.imag == 1 : return str(self.real) + '+' + 'i'
                else : return str(self.real) + '+' + str(self.imag) + 'i'
        
            elif self.imag == 0 : return str(self.real)
        
            else :
                if self.imag == -1 : return str(self.real) + '-' + 'i'
                else : return str(self.real) + '-' + str(abs(self.imag)) + 'i'
            
    # 3 : define add magic method
    def __add__(self , rhs) : # Z1 & Z2
        # replace value on object (real , imag) for output
        real = self.real + rhs.real
        imag = self.imag + rhs.imag
        # return result in class form
        return Complex(real , imag) # will output in a+bi form (calling str method automatically)

    # 4 : define mul magic method
    def __mul__(self , rhs) :
        # update value in new var.
        real = (self.real * rhs.real) - (self.imag * rhs.imag) #ac - bd
        imag = (self.real * rhs.imag) + (self.imag * rhs.real) #ad + bc
        # return result
        return Complex(real , imag) # will output in a+bi form (calling str method automatically
    
    # 5 : define truediv (division complex -> conjugate)
    def __truediv__(self , rhs) :
        # real = (ac + bd) / (c^2 + b^2)
        real = ((self.real*rhs.real) + (self.imag*rhs.imag)) / (rhs.real**2 + rhs.imag**2)
        # imag = (-ad + bc) / (c^2 + d^2)
        imag = (-(self.real*rhs.imag) + (self.imag*rhs.real)) / (rhs.real**2 + rhs.imag**2)
        # return result
        return Complex(real , imag) # will output in a+bi form (calling str method automatically
    
# ---------------------------------------------------------------
## recall class

# 1 : input info
Type , a, b, c, d = [int(x) for x in input().split()]
# 2 : call object
c1 = Complex(a,b)
c2 = Complex(c,d)
# 3 : check type
if Type == 1 : print(c1)
elif Type == 2 : print(c2)
elif Type == 3 : print(c1+c2) # add
elif Type == 4 : print(c1*c2) # multiply
else : print(c1/c2) # division -> conjugate