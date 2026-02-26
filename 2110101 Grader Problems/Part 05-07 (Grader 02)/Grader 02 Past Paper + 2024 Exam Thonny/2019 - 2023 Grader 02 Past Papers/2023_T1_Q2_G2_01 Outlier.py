# 1 : input info
info = [int(e) for e in input().split()]
info = sorted(info) # sort list

# 2 : check length -> even or odd
if len(info) % 2 == 0 : # even
    # split half
    left = info[0 : len(info)//2 : 1]
    right = info[len(info)//2 : : 1]
    # find median -> check len again
    if len(left) % 2 == 0 :
        # beware => 0.5 * (len//2 -1 + len//2)
        Q1 = 0.5 * (left[len(left)//2 - 1] + left[len(left)//2])
        Q3 = 0.5 * (right[len(right)//2 - 1] + right[len(right)//2])
    else :
        Q1 = left[len(left) // 2]
        Q3 = right[len(right) // 2]
    
else : # odd
    # split half
    left = info[0 : len(info)//2 : 1]
    right = info[len(info)//2 + 1 : : 1]
    # find median -> check len again
    if len(left) % 2 == 0 :
        # beware => 0.5 * (len//2 -1 + len//2)
        Q1 = 0.5 * (left[len(left)//2 - 1] + left[len(left)//2])
        Q3 = 0.5 * (right[len(right)//2 - 1] + right[len(right)//2])
    else :
        Q1 = left[len(left) // 2]
        Q3 = right[len(right) // 2]
        
# 3 : find IQR & loop check outlier
IQR = Q3 - Q1
L = Q1 - 1.5*IQR
U = Q3 + 1.5*IQR
outlier = []
# 3.1 : check each element
for ele in info :
    if ele < L or ele > U :
        outlier.append(ele)
     
# 4 : print str -> check len of outlier first
print('L = ' + str(L) + ' ' + 'U = ' + str(U))
if len(outlier) != 0 : 
    print(*outlier) # similar to ','.join(list)
else :
    print('Not found')