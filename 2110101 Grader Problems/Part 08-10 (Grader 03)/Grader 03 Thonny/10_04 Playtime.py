# 1 : loop input info

song = {} # create empty dict
for i in range( int(input()) ) :
    
    # 1.1 : split info first
    name , singer , Type , Time = input().split(', ') # split with ', '
    
    # 1.2 : change time to sec
    minute , sec = int(Time.split(':')[0]) , int(Time.split(':')[1])
    Time = (60 * minute) + sec
    
    # 1.3 : store info in dict (type:time)
    # check if element in dict
    
    # if have -> add value to key
    if Type in song :
        song[Type] += Time
    # else define new key:value in dict
    else :
        song[Type] = Time
        
# 2 : define change time first
def time_format(totalsec) :
    # 2.1 : change time to min & sec first
    minute = totalsec // 60
    second = totalsec % 60
    # 2.2 : check second -> if < 10 -> add 0 before sec
    if second < 10 :
        str_time = str(minute) + ':0' + str(second)
    else : 
        str_time = str(minute) + ':' + str(second)
    # return str_time
    return str_time

# 3 : add element to list & sort
list_playtime = []

# for loop items in dict
for key , value in song.items() :
    # add value to list (of list) then sort
    list_playtime.append( [value , key] )
    
# out of loop -> sort reverse
playtime = sorted(list_playtime , reverse = True)
    # playtime = [ [time,type] , [time,type] , ...]

# 4 : print format
for Time , Type in playtime[0:3] : # index 3 first
    # loop 3 round -> need 3 first
    print(f"{Type} --> {time_format(Time)}") # call fn when print



    
    