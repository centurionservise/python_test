from time import *

start_timer = time() 

struct1 = localtime( start_timer )

print( '\nStarting Countdown At:' , strftime( '%X' , struct1 ) )

i = 10
while i!=0 :
	print( i )
	i -= 1 
	sleep( 1 )

end_timer = time()

difference = round( end_timer - start_timer )

struct2 = localtime( end_timer )
print( '\nEnding Countdown At:' , strftime( '%X' , struct2 ) )

print( '\nRuntime:' , difference , 'Seconds' )