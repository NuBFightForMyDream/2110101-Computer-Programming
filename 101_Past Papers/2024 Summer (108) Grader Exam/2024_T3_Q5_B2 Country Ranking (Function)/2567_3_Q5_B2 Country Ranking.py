#
# 2567_3_Q5_B2: 2567_3_Q5_B2: Country Ranking (Function) 
#

def fahrenheit_to_celsius(F):
    
    return (F - 32) * 5 / 9

def get_perception(temperature):
    
    if temperature >= 35 :
        return 'extreme hot'
    elif 25 <= temperature <= 35 :
        return 'hot'
    elif 20 <= temperature <= 25 :
        return 'comfortable'
    elif -10 <= temperature <= 20 :
        return 'cold'
    else :
        return 'extreme cold'

def print_countries_ranked_by_perception(countries_info):

    # countries_info is list of list
    # for loop each element , rearrange new list first as [ [temp_F , country] ]
    
    sorted_countries_info = []
    for [country_name , temp_F] in countries_info :
        sorted_countries_info.append([temp_F , country_name])
    sorted_countries_info = sorted(sorted(sorted_countries_info , reverse = True))
    
    for ele in sorted_countries_info :
        print(ele)
        

# DO NOT REMOVE or MODIFY THE NEXT 3 LINES
while (cmd:=input().strip()):
    exec(cmd)
    if cmd[-1]==';': break

