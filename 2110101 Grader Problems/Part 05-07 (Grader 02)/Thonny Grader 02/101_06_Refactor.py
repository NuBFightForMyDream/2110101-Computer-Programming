# Key : creaate functions from repeated code

# 1 : fn 1 , read_date -> input str DD MMM YYYY , return [d,m,y]
def read_date():
    month_name =  ["Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    date = input('Enter Date Info : ').split()
# list (of str)
    # index each element in list
    d = int(date[0])
    m = month_name.index(date[1][:3]) + 1 # index 'MMM' then +1 for month nb.
    y = int(date[2])
    # return list
    return [d,m,y]

# 2 : fn 2 , zodiac -> parameter = d,m -> return zodiac name (str)
def zodiac(d,m) :
    if (d >= 22 and m==3) or (d <=21 and m==4) : z = "Aries"
    elif (d >= 22 and m==4) or (d <=21 and m==5) : z = "Taurus"
    elif (d >= 22 and m==5) or (d <=21 and m==6) : z = "Gemini"
    elif (d >= 22 and m==6) or (d <=21 and m==7) : z = "Cancer"
    elif (d >= 22 and m==7) or (d <=21 and m==8) : z = "Leo"
    elif (d >= 22 and m==8) or (d <=21 and m==9) : z = "Virgo"
    elif (d >= 22 and m==9) or (d <=21 and m==10) : z = "Libra"
    elif (d >= 22 and m==10) or (d <=21 and m==11): z = "Scorpio"
    elif (d >= 22 and m==11) or (d <=21 and m==12) : z = "Sagittarius"
    elif (d >= 22 and m==12) or (d <=20 and m==1) : z = "Capricorn"
    elif (d >= 21 and m==1) or (d <=20 and m==2): z = "Aquarius"
    elif (d >= 21 and m==2) or (d <=21 and m==3) : z = "Pisces"
    # return zodiac name
    return z

# 3 : fn3 , day in feb -> parameter = y , return days in that year
def days_in_feb(y) :
    days_feb = 28 # ! caution : better not to rename var. same as fn name
    if (y % 400 == 0 or y % 100 != 0) and (y %4 == 0) :
         days_feb = 29
    # return days_feb (int)
    return days_feb

# 4 : fn4 , day in month -> parameter = m,y -> return day in that month
def days_in_month(m,y) :
    days_in_m = 31
    # check month with 'yon'
    if m==4 or m==6 or m==9 or m==11 :
         days_in_m = 30
    elif m==2 :
         days_in_m = days_in_feb(y) #call fn3 with new parameter y (not same as fn 3)
    # return days_in_m
    return days_in_m

# 5 : fn5 , days_between -> paarameter = d1,m1,y1,d2,m2,y2 -> return int
def days_in_between(d1,m1,y1,d2,m2,y2) :
    days = 0
    if m1 < 12 : days += 31
    if m1 < 11 : days += 30
    if m1 < 10 : days += 31
    if m1 < 9 : days += 30
    if m1 < 8 : days += 31
    if m1 < 7 : days += 31
    if m1 < 6 : days += 30
    if m1 < 5 : days += 31
    if m1 < 4 : days += 30
    if m1 < 3 : days += 31
    if m1 < 2 : days += days_in_feb(y1) # call fn3
    
    if m2 > 1 : days += 31
    if m2 > 2 : days += days_in_feb(y2) # call fn3
    if m2 > 3 : days += 31
    if m2 > 4 : days += 30
    if m2 > 5 : days += 31
    if m2 > 6 : days += 30
    if m2 > 7 : days += 31
    if m2 > 8 : days += 31
    if m2 > 9 : days += 30
    if m2 > 10 : days += 31
    if m2 > 11 : days += 30
    # calculate partial days
    days += (days_in_month(m1,y1) - d1 + 1) + int((y2 - y1 - 1)*365.25) + (d2 - 1)
    # return days
    return days

# 6 ; fn6 : fn main -> call other function , no return -> print instead
def main():
    # call fn1 : read_date
    d1 , m1 , y1 = read_date() # input inside fn1
    d2 , m2 , y2 = read_date() # input inside fn1
    # call fn2 : zodiac
    print( zodiac(d1,m1) , zodiac(d2,m2) )
    # call fn5 : days_between ( fn3 and fn4 were called inside fn5 )
    print( days_in_between(d1,m1,y1,d2,m2,y2) )
    
# 7 : execute input
exec(input().strip()) # strip for error