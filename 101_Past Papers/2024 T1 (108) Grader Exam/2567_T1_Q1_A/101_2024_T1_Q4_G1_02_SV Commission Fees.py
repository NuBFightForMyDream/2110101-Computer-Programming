# 4 appliances -> input n infos -> print commision we got

app1_interest = float(input()) # percent 
app2_interest = float(input()) # percent
app3_interest = float(input()) # percent
app4_interest = float(input()) # percent

n = int(input())
comm_fee = 0

for i in range(n) :
    info = input().split() # [date,type,price]
    # check type
    if info[1] == '1' : comm_fee += (float(info[2]) * app1_interest / 100)
    elif info[1] == '2' : comm_fee += (float(info[2]) * app2_interest / 100)
    elif info[1] == '3' : comm_fee += (float(info[2]) * app3_interest / 100)
    elif info[1] == '4' : comm_fee += (float(info[2]) * app4_interest / 100)
    
# print total commission fee
print(round(comm_fee , 2))