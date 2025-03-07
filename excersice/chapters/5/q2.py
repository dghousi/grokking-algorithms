# 5.2 f(x)=random.random() | not consistent
# Consistency: This function generates a random floating-point number 
# between 0 and 1 each time it is called. Because the output varies with 
# each invocation, it is not consistent.

import random

def f2(x):
    return random.random()

# Example usage
print(f2("apple"))  # Output: A random float between 0 and 1
print(f2("milk"))   # Output: A different random float