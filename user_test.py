import unittest #Importing the unittest module
from user import User #Importing the user class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours .
    Args:
        unittest.Testcase: Testcase class that helps in creating test cases
    '''
    # Items up here .......
    def setUp(self):
        '''
        set up method to run before each test cases.
        '''
        self.new_user = User("Hope","Mbuthye","Daphnee", "mugra","hope.mbuthye21@gmail.com")                                                                           
        # create contact object                 

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Hope")
        self.assertEqual(self.new_user.last_name,"Mbuthye")
        self.assertEqual(self.new_user.username,"Daphnee")
        self.assertEqual(self.new_user.password,"mugra")
        self.assertEqual(self.new_user.email,"hope.mbuthye21@gmail.com")
    

    def test_save_user(self):

        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.user_list),1)


    # Items up here...
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_contact = User("Test", "Hope""Daphnee","mugra","Daphnee21@gmail.com") # new user
        test_contact.save_user()
        self.assertEqual(len(User.user_list),2)


    def test_delete_user(self):

        '''
        test_delete_user method deletes a saved user from the user_list
        '''

        self.new_user.save_user()
        test_user =User("Test", "Hope","Daphnee","mugra" "Daphne21@gmail.com" )
        User.user_list.remove(self)

    def test_find_user_by_user(self):
        '''
        test to check if we can find a user by phone number and display information
        '''

        self.new_user.save_user()
        test_user= User("Test","Hope","Daphnee","mugra","Daphnee21@gmail.com") # new user
        test_user.save_user()
    

        found_user= User.find_by_username("Daphnee")

        self.assertEqual(found_user.username,test_user.username)

    def test_user_exists(self):
        ''' 
        test to checkif we can return a Boolean if we cannot find the user
        '''
        self.new_user.save_user()
        test_user = User("Test","Hope","Daphnee","mugra","Daphnee21@gmail.com") 
        test_user.save_user()

        user_exists = User.user_exists("Daphnee")
        self.assertTrue(user_exists)

    def test_display_all_user(self):
        '''
        method that returns all users  saved
        '''

        self.assertEqual(User.display_users(),User.user_list)







if __name__ == '__main__':
    unittest.main()