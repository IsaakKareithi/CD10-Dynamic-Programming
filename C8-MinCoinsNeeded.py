def min_coins(coins, target):
  dp = [float('inf')] * (target + 1)
  dp[0] = 0

  for coin in coins:
    for val in range (coin, target + 1):
      dp[val] = min(dp[val], dp[val - coin] + 1)

  return dp[target]

# Example usage
coins = [1, 5, 10, 20,]
target_value = int(input("Emter the target value coin: "))
min_coins_needed = min_coins(coins, target_value)
print("The minimum number of coins needed is: ", min_coins_needed)