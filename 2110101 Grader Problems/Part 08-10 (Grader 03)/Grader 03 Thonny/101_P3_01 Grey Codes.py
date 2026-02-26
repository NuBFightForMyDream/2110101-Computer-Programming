# 1 : input n (for 2^n values) & k (for # of elements on each line)
n = int(input())
k = int(input())

# 2 : check condition
if (n < 0 or n > 15) and (k < 0 or k > 100) :
    print('Invalid n and k')
elif (n < 0 or n > 15) :
    print('Invalid n')
elif (k < 0 or k > 100) :
    print('Invalid k')
else :
    # general case
    
    # 3 : print first row zone (1---2---3---)
    out = ''
    for i in range(1 , k+1) :
        # Ex : given len(bit) = 5
        # pattern : 1-9 : - * len(bits each element) = '-----'
        # if n >= 10 : - * (len-1) = '----'
        # last one : '---' -1 from general
        if i == k : # last character (we check for case k = 10+)
            m = n - len(str(i))
        else : # general case
            m = n - len(str(i)) + 1
        # add str to out for each round
        out += str(i) + '-' * m   
    # out of loop -> print out
    print(out)
    
# 4 : define grey codes fn
    # 4.1 : define bits -> list (of str)
    bits = ['0','1']
    # 4.2 : define fn -> gray codes algorithm
    def grey_codes(bits) :
        # 4.3 : reverse list then add each element
        for ele in bits[::-1] :
            bits.append(ele)
        # 4.4 : cut half -> add '0' to lefthalf , add '1' to right half on each element(str)
        for i in range(0 , len(bits)//2 , 1) :
            bits[i] = '0' + bits[i]
        for j in range(len(bits)//2 , len(bits) , 1) :
            bits[j] = '1' + bits[j]
        # 4.5 : return bits after loop
        return bits
    
    # 4.6 : for loop -> n-1 times -> do recur function (parameter changed)
    for i in range(1, n) :
        bits = grey_codes(bits)
    # 4.8 : for loop -> choose 
    loop = 0 # for each round that print
    for i in range(0 , len(bits) , k) :
        loop += 1 # add loop
        print(','.join(bits[i : k*loop : 1]))