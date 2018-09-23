def factorial(inputNumber):
    """Факториал числа — это произведение натуральных чисел от 1 до самого числа (включая данное число). Обозначается факториал восклицательным знаком n!. Факториал нуля и единицы это 1."""
    result=1
    if inputNumber==0 or inputNumber==1:
        return result
    else:
        for i in range(1,inputNumber+1):
            result*=i
        return result


print(factorial.__doc__)
inputNumber=int(input('Input number: '))
print('Factorial for {0} is {1}'.format(inputNumber,factorial(inputNumber)))
