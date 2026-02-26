# 1 : define key of num_info
key_text = {'2':'a' , '22':'b' , '222':'c',
            '3':'d' , '33':'e' , '333':'f',
            '4':'g' , '44':'h' , '444':'i',
            '5':'j' , '55':'k' , '555':'l',
            '6':'m' , '66':'n' , '666':'o',
            '7':'p' , '77':'q' , '777':'r' , '7777':'s',
            '8':'t' , '88':'u' , '888':'v',
            '9':'w' , '99':'x' , '999':'y' , '9999':'z',
            '0':' '}

# 2 : fn text2keys -> change text to key
def text2keys(text) :
    # 2.1 : swap key & value (by adding value:key to reverse_dict)
    text_key = {} # cant directly add to old list (changed while loop X)
    
    # 2.2 : for loop key in dict -> add value:key pair to reverse dict
    for key in key_text :
        text_key[ key_text[key] ] = key # value = num_text[key]

    # 2.3 : for loop : check info in dict
    key_out = ''
    
    for char in text :
        if char.lower() in text_key : # add value to num_out
            key_out += ( text_key[char.lower()] + ' ')
            # change to lower -> find key -> add value + spacebar
    
    # out of loop -> # get last sapcebar out 
    return key_out.strip() 

# 3 : fn keys2text -> change text to key
def keys2text(keys) :
    # 3.1 : for loop -> split text & check key:value
    text_out = ''
    keys_list = keys.split()
    
    for num in keys_list : # num = element
        text_out += (key_text[num]) # add value (from dict) to str
    
    # 3.2 : out of loop -> return text_out
    return text_out

# 4 : execute fn
exec(input().strip())