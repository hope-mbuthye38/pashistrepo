class Credentials :
    '''
    Class that generates new instances credentials
    '''
    pass

    credentials_list = []
    
    def __init__(self,username,email,account,password):
        '''
        __init__method helps us define properties for our project

        Args:
        username : New credentials username
        email : New credentials email
        account : New credentials account
        password : New credentials password
        '''
        self.username = username
        self.email = email
        self.account = account
        self.password = password

    def save_credentials(self):
         '''
         save_credentials method that saves user object into credentials_list
         '''
         Credentials.save_credentials 

    def delete_credentials (self):
        '''
        delete_credentials method deletes a saved user from a credentials_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_username(cls,username):
        '''
        method that finds the users credentials using username

        Args:
            username: find credentials by username
        Return:
            Boolean:True or False depending if the usre exists with that username 

        '''
        for credentials in cls.credentials_list:
            if credentials.username == username:
                return credentials
    
    @classmethod
    def credentials_exist(cls,username):
        '''
        Method that checks if a user exist from the credentials list.

        Args:
            username:Credentials to search if it exists 
        Return:
            Boolean :True or false depending if the user exists
        '''
        for credentials in cls.credentials_list:
            if credentials.username == username:
                return True 

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that return the credentials list
        '''
        return cls.credentials_list
