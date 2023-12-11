terms = int(input("Enter the number of terms: "))

a, b = 0, 1
fib_series = [a, b]

for i in range(2, terms):
    next_term = a + b
    fib_series.append(next_term)
    a, b = b, next_term

print("Fibonacci series up to", terms, "terms:", fib_series)
