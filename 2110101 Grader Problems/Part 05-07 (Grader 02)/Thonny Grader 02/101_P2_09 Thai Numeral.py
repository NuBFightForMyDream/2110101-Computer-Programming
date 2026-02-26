def to_Thai(N) :
    out = ''
    
    # 1 : check digit_10**3 first
    if N >= 1000 : # thousands
        digit_pun = ['soon','neung','song','sam','si','ha','hok','chet','paet','kao']
        out += digit_pun[N//1000] + ' ' + 'pun' + ' '
        N %= 1000 # mod 1000 for check 100s
    
    # 2 : check digit_10**2 
    if N >= 100 :
        digit_roi = ['soon','neung','song','sam','si','ha','hok','chet','paet','kao']
        out += digit_roi[N//100] + ' ' + 'roi' + ' '
        N %= 100 # mod 100 for check 10s
        
    # 3 : check digit_10**1 (case sensitive)
    if N >= 10 :
        digit_sib = ['yi','sam','si','ha','hok','chet','paet','kao'] # in 10**1 digit -> we dont have soon and neung
        # check if N >= 20
        if (N//10) >= 2 : 
            out += digit_sib[N//10 - 2] + ' ' + 'sip' + ' '
        else :
            out += 'sip' + ' '
        N %= 10 # mod 10 for check last digit
    
    # 4 : N < 10 for sure (case sensitive)
    digit_nuay = ['soon','et','song','sam','si','ha','hok','chet','paet','kao']
    out += digit_nuay[(N % 10)]
    
    # 5 : if N == 1 (not by modded) but real value is 1 -> change et to neung
    if out == 'et' :
        out = 'neung'
    
    # 6 : if number is 10's multipliers -> change last word to no string !!dont forget to strip spacebar!!
    if out != 'soon' and len(out) > 4 :
        return out.replace('soon' , '').strip() # strip for spacebar
    
    # 7 : result -> return last result !!dont forget to strip spacebar!!
    return out.strip()

# 8 : execute fn
exec(input().strip())