def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    puddles = [[j, i] for [i, j] in puddles]
    
    dp[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):  
            if i == 1 and j == 1:
                continue 
            elif [i, j] in puddles:
                dp[i][j] = 0
            # 왼쪽 칸, 위 칸 더하기
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
    
    return dp[n][m]
    