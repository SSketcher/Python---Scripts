import time

def fibonacci(n):
        #checking if n is positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    #computing the term
    if n == 1 :
        return 1 
    elif n == 2 :
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print('How many fibonacci numbers do you want to calculate?')
    print('(N must be a positiv intiger)')
    N = input('Pass the number:')
    start = time.time()
    for n in range(1 , int(N)):
        print(n, ":" , fibonacci(n))
    end = time.time()
    print('It took:')
    print(str(end-start) + ' second')