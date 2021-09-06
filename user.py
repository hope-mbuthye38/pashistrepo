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