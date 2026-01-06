def word_break(s, dict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n+1):
        for j in range(i):
            if dp[j] and s[j:i] in dict:
                dp[i] = True 
                break
    return dp[n]

# Example usage
string = 'breakdance'
dictionary = ['break', 'dance']

if word_break(string, dictionary):
    print('The string can be segmented into a dictionary word')
else:
    print("The string cannot be segmented into a dictionary word")
