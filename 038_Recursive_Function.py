# Factorial of a number
def factorial(n):
    if(n == 0):
        return 1
    return n * factorial(n-1)

if __name__ == "__main__":
    n = int(input("Enter n : "))
    print(factorial(n))