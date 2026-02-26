q = list() # queue list
time = list()
n = int(input()) # loop

round = 0

for k in range(n) :
    
    cmd = input().split()
    
    if cmd[0] == 'reset' :
        q.append(int(cmd[1]))
        
        
    elif cmd[0] == 'new' :
        q.append(q[0] + 1)
        # append cmd[1] (time) into time list
        time.append(int(cmd[1]))
        # print ticket n (round = index of q list)
        print('ticket' , q[0] + round)
        round += 1
        
    elif cmd[0] == 'next' :
        print('call' , q[0])
        
    elif cmd[0] == 'order' :
        pass
    
    elif cmd[0] == 'avg_qtime' :
        pass
        # print(round(,))
    