filename = input().strip() # filename
fn = open(filename , 'r')
code = fn.readline() # readline
pattern = fn.readline() # read line
if code == 'T2M' :
    for line in fn :
        pattern = pattern.strip() # pattern
        text = code.strip()
        morse = ''
        for e in text :
             j = pattern.find('[' + e + ']')
             j += 3
             k = pattern.find('[',j)
        morse += pattern[j:k] + ' '
        print(morse.strip())
    
elif code == 'M2T' :
    print('***')
else :
    print('Invalid code')
fn.close() # close file