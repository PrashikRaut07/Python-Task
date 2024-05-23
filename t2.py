def generate_fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

terms = int(input("Enter the number of terms for the Fibonacci sequence: "))     # Get user input    

fib_sequence = generate_fibonacci(terms)        # Generate and display the Fibonacci sequence
print(fib_sequence)