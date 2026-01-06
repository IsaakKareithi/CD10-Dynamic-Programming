def count_paths(maze):
    rows = len(maze)
    cols = len(maze[0])

    # If start or destination is blocked
    if maze[0][0] == 1 or maze[rows - 1][cols - 1] == 1:
        return 0

    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    dp[0][0] = 1

    # Fill first column
    for i in range(1, rows):
        if maze[i][0] == 0:
            dp[i][0] = dp[i - 1][0]

    # Fill first row
    for j in range(1, cols):
        if maze[0][j] == 0:
            dp[0][j] = dp[0][j - 1]

    # Fill rest of the maze
    for i in range(1, rows):
        for j in range(1, cols):
            if maze[i][j] == 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[rows - 1][cols - 1]


# Example maze
maze = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

print("Number of ways to reach destination:", count_paths(maze))
