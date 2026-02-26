# 1 : create piza calories first
pizza_cal = {'PZ871':265.25 , 'PZ953':246.50 , 'Z1983':256.50 , 'Z2853':272.50 , 'LC673':309.25}
customer_info = {} # for storing all customer info

# 2 : input info & store info in list
for i in range( int(input()) ) :
    
    # 2.1 : input name & split info
    total_cal = 0
    inp = input()
    order , info_pizza = inp.split(',')[0] , inp.split(',')[1:]
    
    # 2.2 : calculate dict -> for loop check
    for i in range(0 , len(info_pizza) , 2) :
        
        # check if name in dict
        if info_pizza[i] in pizza_cal :
            
            # define var for easier
            calories = pizza_cal[ info_pizza[i] ] # key = name -> return value = amt of cal
            amount = int(info_pizza[i+1]) # index list
            
            # calculate total calories
            total_cal += (calories * amount) # float * int = float
            
            # add key:value to customer
            # but wait -> check if name ever have in cal?
            if order not in customer_info :
                customer_info[order] = total_cal
            else : # still have customer name
                customer_info[order] += total_cal
            
            # reset total_cal to 0
            total_cal = 0
      
# 3 : for loop sorted dict -> print format
for key in sorted(customer_info) : # sorted(dict) will get list of key only
    print(f"{key} -> {customer_info[key]}")
                