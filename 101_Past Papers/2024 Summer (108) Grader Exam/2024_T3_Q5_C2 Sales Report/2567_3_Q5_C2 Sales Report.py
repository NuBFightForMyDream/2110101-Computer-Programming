#
# 2567_3_Q5_C2: Sales Report 
#

# 1 : input info in this form <name yyyy/mm/dd hh:mm:ss cost>
info = input().split()

# 2 : create dict
most_sales_in_hour = {} # dict

# 3 : while loop input info
while info[0] != 'END' :
    # define splitted info
    name = info[0] ; date = info[1] ; time = info[2] ; cost = float(info[3])
    
    # check if hour is in most_sales_in_hour
    hour = time.split(':')[0] # 'hh'
    if hour in most_sales_in_hour :
        most_sales_in_hour[hour] += cost
    else : # never in dict
        most_sales_in_hour[hour] = cost 
    
    # input info
    info = input().split()
    
# 4 : check most sales
top_sales = 0 ; hour_top = '00'

# 4.1 : create reverse key_value of most_sales_in_hour (to get hour)
reverse_dict_sales = {}
for key in most_sales_in_hour :
    reverse_dict_sales[ most_sales_in_hour[key] ] = key # dict[value] = key


# 4.2 : fo rloop key-valeu & get max value
for hour in most_sales_in_hour :
    # check if more than latest hour
    if most_sales_in_hour[hour] > top_sales : # most_sales_in_hour = cost
        # assign new key (hour) & sales (sales)
        top_sales = most_sales_in_hour[hour]
        
# 5 ; print hour , top_sales
print(reverse_dict_sales[top_sales] , top_sales)
        
        
        
     