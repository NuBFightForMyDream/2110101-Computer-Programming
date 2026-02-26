# 1 : create dict (star:movie)
star2movies = {}
# 1.1 : for loop input info & split
n = int(input())
for i in range( n ) :
    # split info first
    movie_name , star1 , star2 = input().strip().split(', ')
    
    # index 0 -> guaranteed empty dict -> add key:value into dict directly
    if i == 0 :
        star2movies[star1] = [movie_name]
        star2movies[star2] = [movie_name]
        
    else :
        # case 1 : check if star in dict (star1 and star2)
        if star1 not in star2movies :
            # add new key:value into dict
            star2movies[star1] = [movie_name]
        if star2 not in star2movies :
            # add new key:value into dict
            star2movies[star2] = [movie_name]
        
        # case 2 : check if movie_name in dict already? (prevent repeated)
        if (star1 in star2movies) and \
            (movie_name not in star2movies[star1]) :
            # append movie_name to value of key in dict
            star2movies[star1].append(movie_name)
                
        if (star2 in star2movies) and \
            (movie_name not in star2movies[star2]) :
            # append movie_name to value of key in dict
            star2movies[star2].append(movie_name)
            
# cant use else : if ... cuz we have to check if each star in dict
            
# 2 : input name -> strip info
stars = [e.strip() for e in input().split(", ")] # read the last input line
# 2.1 : for loop key in dict
for key in stars:
    if key in star2movies: # check if key in list that we input
         print(key, "->", ", ".join(star2movies[key]))
    else :
         print(key, "->", "Not found")