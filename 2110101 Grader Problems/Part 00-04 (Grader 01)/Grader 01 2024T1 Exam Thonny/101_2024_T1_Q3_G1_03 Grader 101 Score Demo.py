# Given all tasks in grader 2110101 have 100 points

# 1 : input info -> list comp.
info_G1 = [float(e) for e in input().split()]
info_G2 = [float(e) for e in input().split()]
info_G3 = [float(e) for e in input().split()]

# 2 : define list & var. for easier calculation (AQT : Q for Quiz , T for Task)
## Supposing that they don't give more than 5 Tasks Each Quiz

# 2.1 : Grader 01 list & score
## ==> #Task in Q2,Q3 (G1 Retake) will be same -> so using len same as G1

Q1_G1 = info_G1
A11 , A12 , A13 , A14 , A15 = Q1_G1[0:len(Q1_G1)] + [0]*(5 - len(Q1_G1)) # dummy = [0]*2

Q2_G1 = info_G2[0 : len(info_G1) : 1] 
A21 , A22 , A23 , A24 , A25 = Q2_G1[0:len(Q2_G1)] + [0]*(5 - len(Q2_G1))

Q3_G1 = info_G3[0 : len(info_G1) : 1]
A31 , A32 , A33 , A34 , A35 = Q3_G1[0:len(Q3_G1)] + [0]*(5 - len(Q3_G1)) 

# 2.2 : Grader 02 score
## ==> #Task in Q3 (G2 Retake) will be same -> using len start as Q2

Q2_G2 = info_G2[len(info_G1) :  : 1]
B21 , B22 , B23 , B24 , B25 = Q2_G2[0:len(Q2_G2)] + [0]*(5 - len(Q2_G2))

Q3_G2 = info_G3[len(info_G1) : len(info_G2) : 1] # start after G1 , end before G2
B31 , B32 , B33 , B34 , B35 = Q3_G2[0:len(Q3_G2)] + [0]*(5 - len(Q3_G2))

# 2.3 : Grader 03 score
## ==> Task 3 Don't Have Retake
Q3_G3 = info_G3[len(info_G2) :  : 1] # start after G2
C31 , C32 , C33 , C34 , C35 = Q3_G3[0:len(Q3_G3)] + [0]*(5 - len(Q3_G3))

# 3 : calculate score
total_score = max(A11,A21,A31) + max(A12,A22,A32) + \
              max(A13,A23,A33) + max(A14,A24,A34) + max(A15,A25,A35) + \
              max(B21,B31) + max(B22,B32) + max(B23,B33) + max(B24,B34) + max(B25,B35) + \
              C31 + C32 + C33 + C34 + C35

# 4 : print total score
print(int(total_score))