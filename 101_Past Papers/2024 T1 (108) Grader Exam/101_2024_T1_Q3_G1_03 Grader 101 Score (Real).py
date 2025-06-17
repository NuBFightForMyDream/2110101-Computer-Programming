# 1 : Enter Info of each grader quiz first
info_G1 = [float(e) for e in input('Enter Grader 01 Info : ').split()] # 100 points on each task
info_G2 = [float(e) for e in input('Enter Grader 02 Info : ').split()] # 100 points on each task
info_G3 = [float(e) for e in input('Enter Grader 03 Info : ').split()] # 100 points on each task

# 2 : define var. for calculation
# slice info for each grader first
A11 , A12 , A13 = info_G1
A21 , A22 , A23 = info_G2[0 : len(info_G1) : 1]
A31 , A32 , A33 = info_G3[0 : len(info_G1) : 1]

B21 , B22 = info_G2[len(info_G1) : len(info_G2) : 1]
B31 , B32 = info_G3[len(info_G1) : len(info_G2) : 1]

C31 , C32 = info_G3[len(info_G2) : len(info_G3) : 1]

# 3 : calculate formula

# define 2 calculation algorithms
Quiz1_total = 0.15 * (max(A11 , A21 , A31)) + 0.2 * (max(A12 , A22 , A32)) + 0.05*(max(A13 , A23 , A33))
Quiz2_total = 0.05 * (max(B21 , B31)) + 0.05 * (max(B22 , B32))
Quiz3_total = 0.05 * C31 + 0.05 * C32

grader_pts = Quiz1_total + Quiz2_total + Quiz3_total

# -------------------------------------------------------------------------------------------------------
# Next will Calculate Other Score -> return result in total points & grades
midterm = float(input('Enter Midterm Score (60): '))
final = [float(e) for e in input('Enter Final (Choices/50) , (Wiitten(20/20/20) : ').split()]
inclass = float(input('Enter Inclass Assignment Points : '))

midterm_pts = (midterm / 60) * 15
final_pts = (sum(final) / 110) * 20
inclass_pts = (inclass / 100) * 5

total_points = grader_pts + midterm_pts + final_pts + inclass_pts
print('You Got : ' , round(total_points , 2) , 'Points')


