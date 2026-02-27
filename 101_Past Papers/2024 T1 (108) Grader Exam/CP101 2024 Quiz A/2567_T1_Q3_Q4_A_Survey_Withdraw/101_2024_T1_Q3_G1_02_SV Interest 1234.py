# 1 : input info
savings , month = [int(e) for e in input().split()]

# 2 : for loop n times
for i in range(1 , month+1) :
    # Logic : start at month 1 -> start index 1 , end month + 1
    savings += (((i-1)%4)+1)/100 * savings * (1/12)

# 3 : round output & print 
print(round(savings,2))