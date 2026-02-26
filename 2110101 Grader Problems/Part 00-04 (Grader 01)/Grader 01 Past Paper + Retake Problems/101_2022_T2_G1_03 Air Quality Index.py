# 1 : input ingo & set initial info
info_air = [int(e) for e in input().split()]

# 2 : set initial info
air_quality = ['AQI|1 2 3 4 5' , '-------------' , \
               '1..|' , '2..|' , '3..|' , '4..|' , \
               '5..|' , '6..|' , '7..|' , '-------------' ]

# 3 : check case
# pos 0 in info_air -> pos 2 in air_quality list
# start changing at index i+2 (front number is at index i+1)
for pos in range(len(info_air)) : # aqi = each_element
    if info_air[pos] < 25 :
        air_quality[pos+2] = str(pos+1) + '..|+........'
    
    elif 25 <= info_air[pos] < 50 :
        air_quality[pos+2] = str(pos+1) + '..|..+......'
    
    elif 50 <= info_air[pos] < 100 :
        air_quality[pos+2] = str(pos+1) + '..|....+....'
    
    elif 100 <= info_air[pos] < 200 :
        air_quality[pos+2] = str(pos+1) + '..|......+..'
    
    elif info_air[pos] >= 200 :
        air_quality[pos+2] = str(pos+1) + '..|........+'
       
# print each line & strip
for each_line in air_quality :
    print(each_line.strip())