# file = open( 'example.txt' , 'w' )

# print( 'File Name:' , file.name )
# print( 'File Open Mode:' , file.mode )

# print( 'Readable:' , file.readable() )
# print( 'Writable:' , file.writable() )

# def get_status( f ) :
# 	if ( f.closed == True ) :
# 		return 'Closed'
# 	else :
# 		return 'Open'

# print( 'File Status:' , get_status( file ) )
# file.close()
# print( '\nFile Status:' , get_status( file ) )


poem = 'I never saw a man who looked\n'
poem += 'With such a wistful eye\n'
poem += 'Upon that little tent of blue\n'
poem += 'Which prisoners call the sky\n'

with open( 'poem.txt' , 'w' ) as file:
    file.write( poem )
    file.close()

with open( 'poem.txt' , 'r' ) as file:
    print(file.readlines())
    mass_from_file=[]
    # mass_from_file=[]
    for line in file :
        print( line , end = '' )
        mass_from_file.append(line)
    # ccc=file.readlines()
    file.close()

file = open( 'poem.txt' , 'a' )

file.write( '(Oscar Wilde)' )
file.close()

print(mass_from_file)
# print(ccc)


with open( 'poem.txt' , 'r' ) as file:
    ccc=file.readlines()
    # file.close()

print("From readlines:\n",ccc)



