def is_undergrad(sid) :
    # sid = str 10 digit of nisit id
    if (sid[2] == '0') or (sid[2] == '3') or (sid[2] == '4') :
        return True
    # if not undergrad student -> return False
    return False

def get_faculty(sid) :
    # sid = str 10 digit of nisit id
    
    # better way -> create list and use for loop
    faculty_code = ['21','22','23','24','25','26','27','28','29','30',\
                    '31','32','33','34','35','37','38','39','56']
    
    faculty_abbrevname = ['Intania','Arts','Sci','Polsci','Arch','Shi','Edu','Nitade',\
                          'Econ','Med','Vet','Dent','Pharm','Law','FAA','Allied','Psyche','SportSci','BaSCii']
    
    # check 2 last digit of stu_id
    for i in range(len(faculty_code)) :
        if sid[-2:] == faculty_code[i] :
            return faculty_abbrevname[i] # return name of faculty
        
def get_status(sid) :
    # sid = str 10 digit of nisit id
    
    # check cd. by calling fn
    if is_undergrad(sid) == True :
        check_grad = 'U'
    else :
        check_grad = 'G'
        
    fac_name = get_faculty(sid)
    
    return [ check_grad , fac_name ]