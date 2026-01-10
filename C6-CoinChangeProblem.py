def coin_change(coins, ammount):
    # initialize a table to store the minimum number of coins 
    dp = [float('inf')] * (ammount+1)
    dp[0] = 0

    # solve subprobelems for each ammount from 1 to the 
    for i in range(1, ammount+1):
        # try ising each coin denomination
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    if dp[ammount] == float('inf'):
        return -1
    else:
        return dp[ammount]
    
# example usage 
coins = [1, 2, 3]
ammount = int(input("Enter ammount of money: "))

result =  coin_change(coins, ammount)
print(f"The minimum number of coins needed: {result}")