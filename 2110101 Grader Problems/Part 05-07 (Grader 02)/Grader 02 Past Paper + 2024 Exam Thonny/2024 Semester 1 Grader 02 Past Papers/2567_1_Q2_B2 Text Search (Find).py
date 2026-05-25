# P2_10 Text Search
# Chatrphol Ovanonchai

# Sol 1 : using find() method
find_word = input().strip().lower() # lower for case sensitive
num_of_line = int(input())


## Step 1 : Add to string 
## paragraph = []
# list not work : need to check whole word , add to string instead
paragraph_original = "" # for check then refer for new text 
paragraph_to_check = "" 

for _ in range(num_of_line) :
    info = input()
    paragraph_original += info.strip() + "\n" # for new line
    paragraph_to_check += info.lower().strip() + " " # add to whole string
    
## Step 2 : check with find()
## define new string as "result" -> contains string FOUND
pos = 0 # iterator for paragraph
result = "" 

while True : # Until not found 
    # find method start at pos
    pos_found = paragraph_to_check.find(find_word , pos)
    
    # check if found or not (if not found will return -1)
    if (pos_found == -1) :
        # add latest result the break
        result += paragraph_original[pos:]
        break
    
    # normally found
    ## define new found word (refer to original paragraph)
    new_found_word = "<found>" + paragraph_original[pos_found : pos_found + len(find_word)] + "</found>"
    ## add old result (before found) then add new word
    result += paragraph_original[pos:pos_found] + new_found_word ## note : if pos > pos_found will get empty string 
    ## update pos (iterator)
    pos = pos_found + len(find_word)
    
## Step 3 : print out result
print(result.strip())
    
    
    
    
