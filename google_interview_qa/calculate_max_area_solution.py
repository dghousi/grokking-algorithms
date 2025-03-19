def maximalSquare(matrix):
    if not matrix:
        return 0
    
    max_side = 0
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]  # Create a DP table initialized to 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':  # Check for good land
                if i == 0 or j == 0:  # On the first row or first column
                    dp[i][j] = 1  # The largest square can only be 1
                else:
                    # Find the size of the largest square ending at (i, j)
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
                max_side = max(max_side, dp[i][j])  # Update the maximum size

    return max_side * max_side  # Return area of the largest square

# Example usage
matrix = [
    ["0", "1", "0", "1"],
    ["1", "1", "1", "0"],
    ["1", "1", "0", "0"],
    ["1", "1", "1", "1"],
    ["0", "0", "0", "0"]
]

max_area = maximalSquare(matrix)
print("Maximum area of good land is:", max_area)


# Explanation:
    # Initialization: We initialize a dynamic programming table dp with the same dimensions as the input matrix to store the size of the 
        #  largest square ending at each cell.
    # Iterating through the matrix: For each cell that contains a 1, we:
        # If it is in the first row or first column, we can only form a square of size 1.
            # Otherwise, we determine the size of the square that can end at that position by 
        # checking the minimum of the three squares formed by the top, left, and top-left neighbors and adding 1.
    # Calculate Max Area: We track the maximum size found during the iterations and return the area by squaring the maximum size.
        # You can test the function with the example matrix or modify the input as needed