# 1 : input filename & info
doc_info = [] # define list of list
for i in range( int(input()) ) :
    filename = input()
    info = input()
    # add key:value to dict
    doc_info.append([filename , info])
    
# 2 : define search_point fn
def most_search_point(doc_info , word) :
    # parameter = word -> return dict
    
    # 2.1 : create dict for storing score & filename
    score = {} # dict
    # 2.2 : for loop list -> check score on each filename
    for [fn , words] in doc_info :
        # split word
        words = words.split() # list of str
        # define var.
        count_norep = len(set(words)) ; count_rep = len(words)
        times = words.count(word)
        # calculate points
        point = (times / count_rep) * (1 / count_norep)
        # add key:value to dict
        score[point] = fn # key = point , value = filename
    # 2.3 : define max value from dict -> name that have max point
    max_filename = score[max(score)]
    # 2.4 : check score if score = 0
    if max(score) == 0 :
        return 'NOT FOUND'
    return max_filename # else -> return max filename

# 3 : input search word
search_word = input().strip()
while search_word != '-1' :
    # call fn -> find max score
    max_filename = most_search_point(doc_info , search_word)
    print(max_filename)
    # input info at last
    search_word = input().strip()