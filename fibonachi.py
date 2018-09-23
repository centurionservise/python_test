def fibonachi(inputNumber):
    """Последовательность чисел Фибоначчи имеет формулу Fn = Fn-1 + Fn-2. То есть, следующее число получается как сумма двух предыдущих."""
    if inputNumber==0:
        return 0
    elif inputNumber==1:
        return 1
    elif inputNumber==2:
        return 1
    else:
        return fibonachi(inputNumber-1)+fibonachi(inputNumber-2)


print(fibonachi.__doc__)
inputNumber=int(input('Input lenght: '))
print('Fibonachi Row for {0} is {1}'.format(inputNumber,fibonachi(inputNumber)))
