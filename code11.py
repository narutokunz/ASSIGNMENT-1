def fibonacci_sequence(n):
    
    fibonacci_numbers = [0, 1]

    while len(fibonacci_numbers) < n:
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)

    return fibonacci_numbers[:n]


n = int(input("Enter the number of Fibonacci numbers to generate: "))

fibonacci_numbers = fibonacci_sequence(n)

print(f"The first {n} numbers in the Fibonacci sequence are:")
print(fibonacci_numbers)
