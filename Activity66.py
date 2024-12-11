#Write a program to check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not. If it's a palindrome, then it is the same after being reversed.
def palindrone(r):
    reve = len(r)-1
    s = 0
    while s < reve:
        if r[s]!= r[reve]:
            return False
        s += 1
        reve -= 1
    return True


r = (1,2,3,3,2,1)
if palindrone(r):
    print('This tuple is working correctly!')
else:
    print('This is completely wrong!')

