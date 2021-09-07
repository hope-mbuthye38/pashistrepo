class User:
    """
    Class that generates new instances for users
    """
    pass

    user_list = []
     

    def __init__(self,first_name,last_name ,username,password,email):
        '''
        __init__ method that helps us define properties for our objects
        Args:
            first _name : New user first name.
            last_name : New user last name.
            telephone number : New user telephone number.
            email : New user email address.
        '''

        self.first_name = first_name  
        self.last_name = last_name
        self.username = username
        self.password = password 
        self.email = email

         # Empty contact list
 
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)
    
    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_username(cls,username):
        '''
        method that takes in a username and returns a user that matches that username

        Args:
            username:User's to search for
        Return:
            User of person that matches the username.
        '''
        for user in cls.user_list:
            if user.username == username:
                return user

    @classmethod
    def user_exists(cls,username):
        '''
        method that checks if a user exists from the user list

        Args:
            username:User's to search if it exists
        
        Return:
            Boolean:True or false depending if the user exists
        '''

        for user in cls.user_list:
            if user.username == username:
                return False

    @classmethod
    def display_users(cls):
        '''
        method that return the user list
         '''

        return cls.user_list
