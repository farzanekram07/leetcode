# basic recursion
def climbStairs(n):
    if n == 0 or n == 1:
        return 1
    return climbStairs(n-1) + climbStairs(n-2)

n = int(input())
print(climbStairs(n))



# dynamic programming
def climbStair1(n):
    if n == 0 or n == 1:
        return 1
    prev, curr = 1, 1
    for i in range(2, n+1):
        temp = curr
        curr = prev + curr
        prev = temp
    return curr

n = int(input())
print(climbStair1(n))