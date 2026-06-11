# This collects user input
n = int(input("Enter a number: "))

# Conditional statements for printing if there's no prime within the range
if n <= 1:
    print("There are no prime numbers in this range.")
else:
    print(f"Prime numbers between 1 and {n}:")
    
    for num in range(2, n + 1):
        is_prime = True
        
        # Calculate if number is a Prime
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        # Output the result
        if is_prime:
            print(num, end=" ")