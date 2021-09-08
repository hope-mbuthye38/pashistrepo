

from user import User
from credentials import Credentials
def create_user(firstname,lastname,nwname,email,password):
    '''
    Function to create a new user
    '''
    new_user = User(firstname,lastname,nwname,email,password)

    return new_user
def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
def find_user(username):
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_by_username(username)
def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()
def search_user():
    '''
    Function that searches for credentils by username and returns the credentials
    '''
    return User.search_user()
# credentials.......
def create_credentials( Account,username,email,password):
    '''
    Function to create a new credentials
    '''
    new_credentials = Credentials(Account,username,email,password)
    return new_credentials
def save_credential(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()
    # return credentials
def del_credentials(credentials):
    '''
    Function to delete  credentials
    '''
    credentials.delete_credentials()
def find_credentials(username):
    '''
    Function that finds a credentials by username and returns the credentials
    '''
    return Credentials.find_by_username(username)
def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()
def search_credentials():
    '''
    Function that search credentials by username and return the credentials
    '''
    return Credentials.search_credentials()
def main():
    print("Jambo Welcome to your user list.What is your name?")
    user_username = input()
    print(f"Jambo {user_username}. What would you like to do?")
    print('\n')
    while True:
        print("use the short codes to print user: \n cru - create a new user \n du - display user \n fu - find a user \n dlu - delete user \n ex - exit the user list" )
        short_code = input().lower()
        if short_code == 'cru':
            print("New User")
            print("."*200)
            print("First name.......")
            Firstname = input()
            print("Last name........")
            Lastname = input()
            print("username.....")
            Username = input()
            print("Email  ......")
            Email = input()
            print("password......")
            Password =  input()
            

            save_user(create_user(Firstname,Lastname,Username,Email,Password))
        
            print('\n')
            print(f"New user {Username} created" )
            print('\n')
        elif short_code == 'du':
            if display_users():
                print("Here is a list of all your users")
                print('\n')
            for user in display_users():
                    print(f"{user.firstname} {user.lastname} {user.username} {user.email} ")
            else:
                print('\n')
                print("You dont seem to have any account saved yet")
                print('\n')
        elif short_code == 'fu':
            print("Enter the username you want to search for")
            search_username = input()
            if find_user(search_username):
                search_user = find_user(search_username)
                print(f"{search_user.firstname} {search_user.lastname}")
                print('*'*100)
                print(f"username....{search_user.username}")
                print(f"email.....{search_user.email}")
            else:
                print("That user does not exist")
        elif short_code == 'dlu':
            print('\n')
            print("Delete the this user from user_list")
            print(f"{user.u_username} {user.e_address}")
        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't fetch. PLease use the User's short codes")
        #Credentials............*****
            print("Hello Welcome to your credentials list . Whats your account name?")
            user_username = input()
            print(f"Hello {user_username}. what is your intended task?")
            print('\n')
        while True:
            print("Use these short codes to print credentials: \n  cc - create a new credentials \n dc - display credentials \n fc - find credentials \n ec - exit credentials list")
            short_code = input().lower()
            if short_code == 'cc':
                print("New account")
                print("-"*50)
                print("user account ......")
                Account = input()
                print("user account.....")
                username = input()
                print("Email  .....")
                email = input()
                print("Password .....")
                password = input()
                # print(create_credentials(Account,username,email,password))
                save_credential(create_credentials(Account, username,email,password))
                print('\n')
                print(f"New credentials {Account} {username} {email} {password}created")
                print('\n')
            elif  short_code == 'fc':
                print("Input the Account name you want to search ?")
                print('\n')
                search_username = input()
                if find_user(search_username):
                    search_credentials = find_credentials(search_username)
                    print(f"{search_credentials.username}")
                    print('*'*100)
                    print(f"username....{search_credentials.username}")
                    print(f"email.....{search_credentials.email}")
                else:
                    print('\n')
                    print("You dont seem to have any accounts saved yet")
                    print('\n')
            elif  short_code == 'dc':
                if display_credentials():
                    print("Here is a list of all your accounts")
                    print('\n')
                    for credentials in display_credentials():
                        print(f"{Account} {username} {email} {password}")
                        print('\n')
                    else:
                        print('\n')
                        print("you dont seem to have any credentials saved yet")
                        print('\n')
            elif short_code == 'ec':
                print("Adioooos...............!!!")
                break
            else:
                print("I really didn't fetch. Please use the credentials short code")



if __name__ == '__main__':

    main()


    
            