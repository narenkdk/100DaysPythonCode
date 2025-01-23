#Day 61: Dynamic Programming


#Implement dynamic programming for Fibonacci.


def fibonacci(n):
    # Create a list to store Fibonacci numbers up to n
    dp = [0] * (n + 1)
    
    # Base cases
    dp[0] = 0
    dp[1] = 1
    
    # Fill the dp array using the recurrence relation
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

# Test the function
n = 10
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")

