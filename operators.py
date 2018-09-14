# print('Hello, User ',' GongBong',end='!!!\n',sep='+++')
# user_text=input('Please, write something here: ')
# print('Your writen text is - ', user_text)

a=77
b=33

print("Var a=",a,"\tVar b=",b)
print("Operators: +, -, /, *, %, //, **\n")

opereator=input("Enter operator:\t")



if opereator=='+':
    a+=b
    print('Operation: a+=b Result:\t',a)
if opereator=='-':
    a-=b
    print('Operation: a-=b Result:\t',a)
if opereator=='*':
    a*=b
    print('Operation: a*=b Result:\t',a)
if opereator=='/':
    a/=b
    print('Operation: a/=b Result:\t',a)
if opereator=='%':
    a%=b
    print('Operation: a%=b Result:\t',a)
if opereator=='//':
    a//=b
    print('Operation: a//=b Result:\t',a)
if opereator=='**':
    a**=b
    print('Operation: a**=b Result:\t',a)
