import sys
sys.stdin = open('input.txt')
dp = [0]*(50)
n = int(input())

for i in range(n):
    dp[i] = i

print(dp)

for i in range(2,n):
    j = 1

    while j**2 <= i:

        a = dp[i]
        b = dp[i-j**2]+dp[j**2]
        dp[i] = min(dp[i],dp[i-j**2]+dp[j**2])
        j += 1

print(dp)




# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
# 1 2 3 1 2 3 4 2 1  2  3  3  2  3  4  1  2  3  4  2  3  4  5  3  1

