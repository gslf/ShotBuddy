class User():
    """ A class to represent a TwitterIT user
    Attributes:
		id              User identificator
        username        Username
        password        User password
    """

    def __init__(self, username, id='', password=''):
        self.id = id
        self.username = username
        self.password = password


    def toDictionary(self):
        """ A function that return all attribs in a dictionary

        Return:
            object (dictionary) - {attrib1: value1, attrib2: value2, . . . }
        """

        object_dict = {
            'id' : self.id,
            'username' : self.username,
            'password' : self.password,
        }
       
        return object_dict


    def is_active(self):
        """ Flask-login - all users are active
        """
        return True


    def get_id(self):
        """ Flask-login - use username as id
        """
        return self.username


    def is_authenticated(self):
        """ Flask-login - authentication flag
        """
        return True


    def is_anonymous(self):
        """ Flask-login - anonymous users aren't supported
        """
        return False
