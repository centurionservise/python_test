import pickle, os

file_users='users.dat'

def isFile(file_name):
    return True if os.path.isfile( file_name ) else False

def print_users(users_list):
    counter=1
    for cur_user in users_list:
        print('User {} -> '.format(counter),end=' ')
        # print('*********')
        print('Name: ',cur_user['name'],end=', ')
        print('Age: ',cur_user['age'],end=', ')
        print('Sex: ',cur_user['sex'])
        counter+=1



data_users = []
user={}

if not isFile(file_users) :
    print("\nNo file No Users Data....")
    with open( file_users , 'wb' ) as file:
            pickle.dump( data_users , file )
    if isFile(file_users):
        print("An empty file was created")
else :
    print("\nUser Data File Present")
    # answer=input("Do you want to get users from file (y/n)?: ")
    # if answer=='y':
    with open( file_users , 'rb' ) as file:
        data_users = pickle.load( file )
    if data_users:
        print("User Data Loaded")
            # print( 'Users List from file:\n' , data_users )
            # print_users(data_users)
        # else:
            # break

while True:
    print("\n")

    if data_users==[]:
        print("1 - Add User")
        # print("2 - Remove User")
        # print("3 - View List\n")
        print("4 - Exit programm")
    else:
        print("1 - Add User")
        print("2 - Remove User")
        print("3 - View List")
        print("4 - Exit programm")

    

    answer=input("\n(1-4)?: ")
    print("\n")

# ADD USER
    if answer=='1':

        with open( file_users , 'rb' ) as file:
            data_users = pickle.load( file )

        user['name']=input("Enter User Name: ")
        user['age']=input("Enter User Age: ")
        user['sex']=input("Enter User Sex: ")
        print("\n")

        if user in data_users:
            print("*** This user is present ***")
            continue
        data_users.append(user)
        print_users(data_users)

        with open( file_users , 'wb' ) as file:
            pickle.dump( data_users , file )

# EXIT
    if answer=="4":
        # print("Buy-buy")
        break

# Remove USER
    if answer=="2":
        if data_users==[]:
            print("Data_user==[]")
            continue

        counter=0
        for i in data_users:
            counter+=1
        print("Amount of users in DB: ",counter)

        answer=input("Which user to remove ?: ")
        
        if (int(answer) in range(counter+1)) and int(answer)!=0:
            print("*** Good choise ***")
        else:
            print("*** Wrong way ***")
            continue

        del data_users[int(answer)-1]
        with open( file_users , 'wb' ) as file:
            pickle.dump( data_users , file )

# View List
    if answer=='3':
        if data_users==[]:
            print("Data_user==[]")
            continue
        print_users(data_users)