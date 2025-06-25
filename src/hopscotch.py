def hopscotch(num_steps):
    """HOPSCOTCH

    This problem was asked by Amazon.
    Difficulty: Hard

    There exists a staircase with N steps, and you can climb up either 1 or 2
    steps at a time. Given N, write a function that returns the number of
    unique ways you can climb the staircase. The order of the steps matters.
    For example, if N is 4, then there are 5 unique ways:
    * 1, 1, 1, 1
    * 2, 1, 1
    * 1, 2, 1
    * 1, 1, 2
    * 2, 2
    What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?
    For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
    """
    # Classic staircase problem: ways to climb N steps using 1 or 2 steps at a time
    # This is essentially the Fibonacci sequence: f(n) = f(n-1) + f(n-2)

    if num_steps <= 0:
        return 0
    if num_steps == 1:
        return 1
    if num_steps == 2:
        return 2

    # Dynamic programming approach
    dp = [0] * (num_steps + 1)
    dp[0] = 1  # One way to climb 0 steps (don't climb)
    dp[1] = 1  # One way to climb 1 step

    for i in range(2, num_steps + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[num_steps]


def hopscotch_varied_steps(num_steps, steps_set):
    """HOPSCOTCH WITH VARIED STEPS
    
    Generalized version of the hopscotch problem where you can climb
    any number of steps from a given set of positive integers.
    
    Args:
        num_steps (int): Total number of steps to climb
        steps_set (set or list): Set of allowed step sizes
    
    Returns:
        int: Number of unique ways to climb the staircase
    
    Examples:
        hopscotch_varied_steps(4, {1, 2}) -> 5
        hopscotch_varied_steps(4, {1, 3, 5}) -> 3
    """
    if num_steps < 0:
        return 0
    if num_steps == 0:
        return 1  # One way to climb 0 steps (don't climb)
    
    # Convert to sorted list for consistent iteration
    if not steps_set:
        return 0  # No steps allowed, impossible to climb
    
    steps_list = sorted(steps_set)
    
    # Dynamic programming approach
    # dp[i] = number of ways to reach step i
    dp = [0] * (num_steps + 1)
    dp[0] = 1  # Base case: one way to reach 0 steps
    
    for i in range(1, num_steps + 1):
        # For each position i, sum up ways to reach it from all possible previous positions
        for step in steps_list:
            if step <= i:  # Can only use this step size if we have enough steps
                dp[i] += dp[i - step]
    
    return dp[num_steps]
