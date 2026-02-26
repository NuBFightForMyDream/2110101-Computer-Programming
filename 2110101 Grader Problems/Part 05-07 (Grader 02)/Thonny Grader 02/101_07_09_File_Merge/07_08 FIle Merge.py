# 1 : define fn read_next : parameter = filename -> return stu_id , grade
def read_next(file) : # read each line
    while True : # Always Do
        # 1.1 : read each line
        line = file.readline()
        if len(line) == 0 :
            break # if end -> break loop read
        # 1.2 : split into stu_id & grade
        info = line.strip().split() # info[0] , info[1]
        if len(info) == 2 : # check info in that line
            return info[0] , info[1]
    # 1.3 : out of loop -> break from len = 0
    return '' , ''
## dont forget do define fn before reading files
        
# 2 : read 2 files 
    
# 2.1 : read 2 files together
filename1 , filename2 = input().split()
file1 = open(filename1 , 'r') # data1.txt
file2 = open(filename2 , 'r') # data2.txt

# 2.2 : call fn above for read line filename1 & filename2 (read first line)
stu_id1 , gpa1 = read_next(file1) 
stu_id2 , gpa2 = read_next(file2)
    
### 3 : Key : compare line on each file -> if line 1 before line 2 -> use read_next fn
# Logic : check fac_num -> check academic yr -> check other number

# 3.1 : check faculty number
while (stu_id1 != '' and stu_id2 != '') : # still do loop -> break if 2 files are vacant
    # case 1 : same faculty 
    if stu_id1[-2:] == stu_id2[-2:] :
        # check academic year 
        if stu_id1[0:2] < stu_id2[0:2] : # pp1 before pp2 -> print stu , grade -> read next line
            print(stu_id1 , gpa1) # print old value
            stu_id1 , gpa1 = read_next(file1) # replace new value (next line)
        
        elif stu_id1[0:2] > stu_id2[0:2] : # stu_id1[0:2] >= stu_id2[0:2]
            print(stu_id2 , gpa2)
            stu_id2 , gpa2 = read_next(file2)
            
        else : # stu_id1[0:2] == stu_id2[0:2] (ssame fac_num & same academic yr)
            # check other number -> [2:-2] (no case same id)
            if stu_id1[2:-2] > stu_id2[2:-2] :
                print(stu_id2 , gpa2) # print old value
                stu_id2 , gpa2 = read_next(file2) # update value
            else :
                print(stu_id1, gpa1) # print old value
                stu_id1 , gpa1 = read_next(file1) # update value
    
    # case 2 : fac_num1 is less than fac_num2       
    elif stu_id1[-2:] < stu_id2[-2:] : # print fac1_num first
        print(stu_id1 , gpa1)
        stu_id1 , gpa1 = read_next(file1)
    
    # case 3 : fac_num1 is more than fac_num2 
    elif stu_id1[-2:] > stu_id2[-2:] :
        print(stu_id2 , gpa2) # print old value
        stu_id2 , gpa2 = read_next(file2) # update value
    
# 4 : out of loop -> check if one of two files are vacant
while stu_id1 != '' :
    print(stu_id1 , gpa1) # print old value
    stu_id1 , gpa1 = read_next(file1) # update value  
while stu_id2 != '' :
    print(stu_id2 , gpa2) # print old value
    stu_id2 , gpa2 = read_next(file2) # update value
    
# 5 : close file
file1.close()
file2.close()