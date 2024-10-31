def fibonacci(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1  # Start with the first two Fibonacci numbers
        for _ in range(2, n + 1):
            a, b = b, a + b  # Update a and b for the next Fibonacci number
        return b  # b is now the nth Fibonacci number

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')