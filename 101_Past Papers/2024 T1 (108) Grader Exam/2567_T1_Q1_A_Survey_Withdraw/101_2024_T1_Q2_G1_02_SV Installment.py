# 1 : input info
balance = float(input().strip()) # balance P Baht
rate = float(input().strip()) # Rate R per year
installment = float(input().strip()) # paid M baht per month
paid_month = 0
total_interest = 0

# 2 : while loop
while balance > installment :
    
    interest = (rate / 100) * balance / 12
    
    if installment < interest :
        break
    
    else : 
        paid_month += 1
        total_interest += interest
        balance -= (installment + interest)
    
print(paid_month)