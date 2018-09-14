def fibonacci_generator() :
    a = 0
    b=1
    while True :
        yield a
        a , b = b , a + b

# fib = fibonacci_generator()

# max_number - до какого максимального числа высчитывать
def fibonacci1(max_number):
    fib = fibonacci_generator()
    print("\nFibonacci 1 / max_number\n")
    count=1
    for i in fib :
        if i >max_number:
            break
        else :
            print( 'Generated: %d'%count , i )
            count+=1

# iter - сколько раз высчитывать число фибоначи
def fibonacci2(iter):
    fib = fibonacci_generator()
    print("\nFibonacci 2 / iter\n")
    for i in range(iter) :
        print( 'Generated %d:'%i , next(fib) )

# fibonacci1(200)
# fibonacci2(50)
