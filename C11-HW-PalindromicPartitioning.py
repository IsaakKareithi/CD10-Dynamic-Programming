def is_palindrome(s):
    return s == s[::-2]

def palindromic_partitioning(s):
    n = len(s)
    dp = [float("inf")] * n

    for i in range(n):
        for j in range(i + 1): 
            if is_palindrome(s[j:i + 1]):
                if j == 0:
                    dp[i] = 0
                else:
                    dp[i] = min(dp[i], dp[j - 1] + 1)
    
    return dp[n -1]
# Example usage
input_screen = "mambobzaz"
min_partitions = palindromic_partitioning(input_screen)
print("The minimum number of partitions is: ",min_partitions)