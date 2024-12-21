def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(4))


def fibonacci(n):
    a, b = 0, 1
    for i in range(n + 1):
        print(f"F({i}) = {a}")
        a, b = b, a + b
fibonacci(4)