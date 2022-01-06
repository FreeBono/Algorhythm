import sys
sys.stdin = open('input.txt')

n = int(input())
dp = [0]*(100001)
for k in range(100001):
    dp[k] = k


dp[1] = 1

for i in range(2,100001):
    j = 1

    while j**2 <= i:
        a = dp[j ** 2]
        b = dp[i-(j**2)]
        dp[i] = min(dp[i-j**2]+1,dp[i])

        j += 1


print(dp[n])




# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
# 1 2 3 1 2 3 4 2 1  2  3  3  2  3  4  1  2  3  4  2  3  4  5  3  1

