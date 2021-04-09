import time

#Using dictionary to create cache for the function
fibonacci_cache = {}

def fibonacci(n):
    #Checking if n is positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    #Chcecking if the valeu is in the cache 
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    #Computeing the term
    if n == 1 :
        valeu =  1 
    elif n == 2 :
        valeu = 1
    elif n > 2:
        valeu = fibonacci(n - 1) + fibonacci(n - 2)
        
    #Adding the term to cache
    fibonacci_cache[n] = valeu
    return valeu


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