# 1 : input check word
check = input()
orgtext = '' # for output
copytext = '' # for check
for i in range( int(input()) ) :
    # add text to orgtext & copytext
    info = input()
    orgtext += info + '\n' # for new line
    copytext += info + ' ' # add space for check
    
# while loop -> check alphabet
k = 0
out_text= '' # for output
while k < len(orgtext) : # check len to orgtext (not copytext)
    # check if found text
    if copytext[k:k+len(check)].lower() == check.lower() :
        # add orgtext
        out_text += '<found>' + orgtext[k:k+len(check)] + '</found>'
        k += len(check)
    else : # not same -> add normal text
        out_text += orgtext[k]
        k += 1
# print out_text
print(out_text)
    