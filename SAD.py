def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Initialize the sequence with the first two numbers
    sequence = [0, 1]
    
    # Loop to calculate the next numbers
    for _ in range(2, n):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
        
    return sequence

# Example usage:
print(fibonacci_iterative(100))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
