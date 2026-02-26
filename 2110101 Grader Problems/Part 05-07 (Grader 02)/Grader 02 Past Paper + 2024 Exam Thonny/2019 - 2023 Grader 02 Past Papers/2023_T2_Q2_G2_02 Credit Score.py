# 1 : create list
points = []
# input info & add [price , name] into list
for i in range(int(input())) : 
    info = input().split()
    points.append([int(info[1]) , info[0]]) # append list of list
# sort reverse
points.sort(reverse = True)  

# 2 : input credit_in & check price in loop
credit = int(input()) # credit in (will be changed to out)
credit_paid = 0 
result = []
# 2.1 : check element in points list -> check if it can redeem
for i in range(len(points)) :
    rounds = 0 # for nb. of cards (can't more than 3)
    while (credit // points[i][0] > 0) and (rounds < 3) : # check by // element -> if > 0 , can redeem
        # if can redeem -> add round & subtract pts.
        rounds += 1
        credit_paid += points[i][0] # pts
        # subtract credit if can paid
        credit -= points[i][0]
    # add sublist to list
    if rounds >= 1 : # append only cards that can redeemed
        result.append([points[i][1] , str(rounds)])

# 3 : sort list & print each element
result = sorted(result)
# print credit : credit_all = credit(out) + credit_paid
print('>' , str(credit + credit_paid) , str(credit_paid) , str(credit))
# check if result is [] or not
if result == [] :
    print('No coupon')
else : 
    for ele in result :
        print(' '.join(ele)) # join ' '