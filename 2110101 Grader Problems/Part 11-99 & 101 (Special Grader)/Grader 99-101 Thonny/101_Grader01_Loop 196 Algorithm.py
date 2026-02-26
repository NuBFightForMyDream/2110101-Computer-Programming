# 1 : input number
number = int(input())
num_list = []

# 2 : define fn for checking palindrome?
def is_palindrome(number) :
    # return True if number is palindrome , else return false
    ## split str num into half (hleft , hright) then check reverse
    halfleft = str(number)[] ; halfright = str(number)[]