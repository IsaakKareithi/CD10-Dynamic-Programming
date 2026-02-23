# Matrix chain multiplication
def matrix_chain_multiplication(A):
    n = len(A) - 1
    dp = [[float("inf")] * n for _ in range(n)]

    # Base case: chain length l (no multiplication needed for single matrices)
    for i in range(n):
        dp[i][i] = 0

    for l in range(2, n + 1): # Chain length from 2 to n 
        for i in range(1, n-1+2): 
            j = i + l - 1
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + A[i-1] * A[k] * A[j])

    return dp[1][n-1]

# Example usage
matrix_dimensions = [10, 30, 5, 60]
min_scalar_multiplications = matrix_chain_multiplication(matrix_dimensions)
print('The minimum scalar multplications needed are: ', min_scalar_multiplications)