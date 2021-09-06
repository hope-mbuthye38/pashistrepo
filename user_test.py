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

if __name__ ==  '__main__':
    unittest.main()

    # Items up here...

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_contact = User("Test","Daphnee","mugra","test@user.com") # new contact
            test_contact.save_user()
            self.assertEqual(len(User.user_list),2)

if __name__ == '__main__':
    unittest.main()