# def serg_func(x,y,z=100):
#     print("Hello")
#     print("x= %d y=%d z=%d"%(x,y,z))
#     result=x+y+z
#     print("Result: %d"%result)
#     str_temp='77MM'
#     print(str_temp.isdigit())


# serg_func(z=10,x=33,y=300)

# def changeme( mylist ):
#    "Это изменяет список в этой функции"
# #    mylist = [1,2,3,4] # This would new reference in mylist
#    mylist[0]=555
#    print ("Значения внутри функции: ", mylist)
#    return

# mylist = [10,20,30]
# changeme( mylist )
# print ("Значения вне функции: ", mylist)


# def printinfo( arg1=1, *vartuple ):
#    print ("Вывод: ")
#    print ('arg1: ',arg1)
#    for index, value in enumerate(vartuple):
#       print ('index=',index, 'value=',value)
#    return

# printinfo( 10 )
# printinfo(160, 'OPPP' )

# import itertools
# horses = [1, 2, 3, 4]
# races = itertools.permutations(horses)
# print(races)
# print(list(itertools.permutations(horses)))

string="ABCDEFG"

def incrementer(string) :
    i = 0
    while i<len(string) :
        yield string[i]
        i += 1

inc=incrementer(string)

print( next( inc ) )
print( next( inc ) )
print( next( inc ) )
print( next( inc ) )
print( next( inc ) )


