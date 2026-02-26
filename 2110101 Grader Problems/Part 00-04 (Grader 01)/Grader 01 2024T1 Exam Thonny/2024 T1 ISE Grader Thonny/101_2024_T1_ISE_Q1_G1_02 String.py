# 1 : input string
info = input().strip().split()

# 2 : reverse first
for i in range(len(info)) :
    # reverse in ele -> set first char to upper , else lower
    firstletter_reverse = info[i][::-1][0].upper()
    otherletter_reverse = info[i][::-1][1:].lower()
    # change each char
    info[i] = firstletter_reverse + otherletter_reverse
    
# 3 : join list of str to str
print(' '.join(info))