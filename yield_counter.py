def counter() :
    i = 1
    while True:
        yield i
        i += 1

count=counter()

temp_number=10

for zz in range(temp_number):
    call_amount=next(count)
    print(call_amount)

print("Call amount: ",call_amount)