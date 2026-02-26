# Prog-08: Bag-of-words

def read_stopwords():
    file = open('stopwords.txt', 'r'); stop_words = ''
    for i in [e.strip() for e in file.readlines()]:
        stop_words += i+' '
    file.close()
    return stop_words.split()

def read_file(file_name):
    file = open(file_name, 'r'); temp = ''
    for i in [line.strip() for line in file.readlines()]:
        temp += i+' '
    file.close(); words = ''
    for i in temp:
        if i.isalnum() == False:
            words += ' '
        else:
            words += i
    return words.lower()

def alphanum_count(file_name):
    c = 0
    for i in read_file(file_name):
        for e in i:
            if e.isalnum() == True:
                c += 1
    return c

def line_count(file_name):
    file = open(file_name, 'r')
    temp = file.readlines()
    file.close()
    return len(temp)

def char_count(file_name):
    file = open(file_name, 'r'); temp = []; c = 0
    for i in [line for line in file.readlines()]:
        if '\n' in i:
            c += 1
        temp += i
    file.close()
    return len(temp) - c

def main(file_name):
    print('-------------------')
    print('char count =', char_count(file_name))
    print('alphanumeric count =', alphanum_count(file_name))
    print('line count =', line_count(file_name))
    print('word count =', len(read_file(file_name).split()))

def words_nostop(file_name):
    words = []
    for i in read_file(file_name).split():
        if i in read_stopwords():
            words += []
        else:
            words += [i]
    return ' '.join(words)

def BoW(file_name):
    x = []; y = []; bow = []
    for i in words_nostop(file_name).split():
        if i not in x:
            x.append(i)
            y.append(1)
        else:
            y[x.index(i)] += 1
    for i in range(len(x)):
        bow.append([x[i], y[i]])
    return sorted(bow)

def fhash(w, M):
    c = 0
    for i in range(len(w)):
        c += ord(w[i])*37**i
    return c % M

def BoW_fhash(file_name, M):
    y = []; x = []; z = []; bow = []
    for i in range(len(words_nostop(file_name).split())):
        y.append(fhash(words_nostop(file_name).split()[i], M))
    for i in range(len(y)):
        if y[i] not in x:
            x.append(y[i])
            z.append(1)
        else:
            z[x.index(y[i])] += 1
    for i in range(len(x)):
        bow.append([x[i], z[i]])
    return sorted(bow)

#-----------------------------------------------------

# file_name = input('File name = ')
# use_fh = input('Use feature hashing ? (y,Y,n,N) ')
# while use_fh not in 'nNyY':
#     print('Try again.')
#     use_fh = input('Use feature hashing ? (y,Y,n,N) ')
# if use_fh in 'Yy':
#     M = int(input('M = '))
#     main(file_name)
#     print('BoW =', BoW_fhash(file_name, M))
# else:
#     main(file_name)
#     print('BoW =', BoW(file_name))
print(words_nostop('sample.txt'))