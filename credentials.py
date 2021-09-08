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
