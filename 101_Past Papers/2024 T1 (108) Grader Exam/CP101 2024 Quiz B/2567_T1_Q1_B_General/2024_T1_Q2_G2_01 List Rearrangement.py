info = [int(e) for e in input().split()]
order = sorted(info) # sort for order
out = [] # for output 

sum_start = 1 # given first sum = 1
for ele in order :
    sum_start += ele # plus for each round
    # find pos. by -1 then mod (Ex : 5-1 % 3 = 1 = id2 (safer for index -1)
    end = info[(sum_start-1) % len(info)] # -1 because start with round = 1
    # pop element that ban & update to list
    ban = info.pop((sum_start-1) % len(info)) # .pop(pos.)
    # append ban to out list
    out.append(ban)
# join list of int with *
print(*out)