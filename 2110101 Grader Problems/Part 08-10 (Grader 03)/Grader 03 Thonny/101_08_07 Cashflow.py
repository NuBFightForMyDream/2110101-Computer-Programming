def total(pocket) : # return money in pocket
    # define total 
    total = 0
    # for loop key -> add to total
    for key in pocket :
        total += (pocket[key] * key)
    # out of loop -> return total
    return total

def take(pocket , money) : # add money to pocket(dict)
    # for loop key in money_in -> check if in pocket
    for key in money :
        if key in pocket :
            pocket[key] += money[key] # add value to pocket
        else :
            pocket[key] = money[key] # add new key:value to dict
    # out of loop -> return pocket        
    return pocket

def pay(pocket , amt) :#  return amount paid & amount left
    # check if amt is less than money in pocket
    if amt > total(pocket) :
        paid = dict() # can't pay
    
    else : # general case -> check money in pocket first
        # 1 : define money list (check each char) & paid dict
        money = [1000,500,100,50,20,10,5,2,1]
        paid = {e:0 for e in money} # dict comp. -> given each bank have 0
        
        # 2 : for loop each bank in money -> check cd.
        for each_money in money :
            while amt // each_money >= 1 and each_money in pocket
                \ and pocket[each_money] > 0 : # cd : devided , in pocket , have that bank
                   
                paid[each_money] += 1 # add key:1 in paid
                pocket[each_money] -= 1 # subtract key:1 in pocket
                amt -= each_money # change amount
        
        # 3 : need only val > 0 in paid dict (dict comp.)
        paid = {k:v for k,v in paid.items() if v > 0}
    
    # 4 : return paid dict
    return paid
    
# execute input
exec(input().strip())