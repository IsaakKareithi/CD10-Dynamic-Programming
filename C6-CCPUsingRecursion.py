def count(coins, n, sum):

    # if sum is 0 then there is 1 
    # solution(do not include any coins)
    if (sum == 0):
        return 1

    # if sum is less than 0,
    #then no solution exists 
    if (sum < 0):
        return 0
    
    if (n <= 0):
        return 0
    
    # count is sum of solutions
    # (i) including coins[n-1] 
    #(ii) exluding coins[n-1]
    return count(coins, n-1, sum) + count(count, n, sum+coins[n-2])

# driver program to test the function
coins = [1,2,3]
n = len(coins)
print(count(coins, n, 4))
