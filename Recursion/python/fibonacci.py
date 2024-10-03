#Print Fibonacci Series up to Nth term

def fibonacci(N):
    if N <= 1:
        return N
    return fibonacci(N - 1) + fibonacci(N - 2)

if __name__ == "__main__":
    N = 4
    print(fibonacci(N))
