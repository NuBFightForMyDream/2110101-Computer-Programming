# 1 : input filename & cmd
filename = input().strip()
cmd = input().strip()

# 1.1 : check cmd first
if cmd not in ['LSTRIP','RSTRIP','STRIP','STRIP_ALL'] :
    print('Invalid command')
    exit(0) # exit program immediately -> not doing next cmd
    