# 1 : define 2 fns
def hide_vowel(word) : # w = offensive words (str)
    # define for output
    out = ''
    # for loop -> check if found vowel -> replace with *
    for char in word :
        if char.lower() in 'aeiou' :
            char = '*'
        # add value to char every time
        out += char
    # out of loop -> return out
    return out
    
def less_offensive(text , oword) : # text = all string , oword = word we need to censor
    # while loop until last char
    k = 0
    # define var.
    copytext = text # define copytext for changing
    out_text = ''
    while k < len(text) :
        if copytext[k : k+len(oword)].lower() == oword.lower() :
            # change word we're checking (dont use oword)
            out_text += hide_vowel(text[k:k+len(oword)])
            # we've to output original text -> we'll change parameter to word that we're checking
            k += len(oword) # skip with len(oword) pos.
        else :
            out_text += text[k]
            k += 1
    # return out_text
    return out_text

# 2 : input & output zone
Owords = input().split()
text = input()
# while loop for owords that have more than 1 -> replace old string
for ele in Owords :
    text = less_offensive(text , ele)
# output -> print latest text
print(text)