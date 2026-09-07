def fibonacci(n, memo):
    if n == 0:
        return 0

    if n == 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    return memo[n]


n = int(input("Enter n: "))
memo = {}

result = fibonacci(n, memo)

print("fibonacci number:", result)

print(memo)
