# define 3 fns
# fn 1 : gcd
def gcd(a,b) :
    while b != 0 :
        a , b = b , (a % b) # euclidean algoruithm : swap & find new value (by mod)
    # out of loop -> b = 0 -> return least common divider = a
    return a # if no gcd -> return last value = 1

# fn 2 : check if 3 numbers are coprime number
    # logic : all gcd = 1 -> gcd pair then gcd
def is_coprime(a,b,c) :
    if gcd( gcd(a,b) , gcd(b,c) ) == 1 : 
        return True
    return False # if GCD is not 1

# fn 3 : pythagorean triple in range max_len
def primitive_Pythagorean_triples(max_len) :
    # Logic : return sublist that have [a,b,c]
    # which is side of pythagorus triangle & gcd = 1
    # !! sort ascending by c first -> if c equal , sort ascending by a !!
    
    # 1 : create empty list first
    triple = []
    
    # 2 : for loop begin a then b (range b starts with a cuz it has to be longer)
    for a in range(2 , max_len) :
        for b in range(a , max_len) :
            # c = hypoteneuse side = sqrt(a^2 + b^2) 
            c = (a**2 + b**2)**(0.5)
            
            # Check CD : coprime , c < len , c is int
            if is_coprime(a,b,c) == 1 and (c <= max_len) and (c % 1 == 0) :
                triple.append( [int(c),b,a] ) # append [c,b,a] to triple
    
    # 3 : sort then reverse to [a,b,c]       
    triple = sorted(triple)
    for i in range(len(triple)) :
        triple[i] = triple[i][::-1] # reverse char in element
        
    # 4 : check if c equal -> sort by a (swap elements)
    for i in range(len(triple) - 1) :
        if triple[i][2] == triple[i+1][2] : # c1 = c2
            if triple[i][0] > triple[i+1][0] : # a1 > a2 => swap
                triple[i] , triple[i+1] = triple[i+1] , triple[i] # swap [a,b,c]
    
    # 5 : out of loop -> return triple list (of list)
    return triple

# 4 : execute fn
exec(input().strip())