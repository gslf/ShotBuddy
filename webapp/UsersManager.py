from werkzeug.security import generate_password_hash, check_password_hash
from webapp import login
from webapp.DBManager import DBManager
from webapp.User import User

@login.user_loader
def load_user(username):
    db = DBManager()

    # Retrieve user details
    db.open()
    users = db.select('SELECT * FROM users WHERE username=?',(username,))
    db.close()


    if len(users) > 0:
        user_id = users[0][0]
        user = User(username, user_id)

        return user
    return None


class UsersManager():
    """ Users management interface
    Attributes:
        user (User)     The user object
        db (DBManager)  The database manager object
    """

    def __init__(self, user=None):
        self.user = user
        self.db = DBManager()

    def fetch(self):
        """ Check if user are in DB
        Return:
            result (boolean)
        """
        self.db.open()
        results = self.db.select('SELECT username FROM users WHERE username=?', (self.user.username,))
        self.db.close()

        if len(results) > 0:
            return True
        else:
            return False


    def check(self):
        """ Check if user/pwd are in DB
        Return:
            result (boolean)
        """
        self.db.open()
        results = self.db.select(
            'SELECT * FROM users WHERE username=?', (self.user.username,))
        self.db.close()

        if len(results) > 0:
            if check_password_hash(results[0][2], self.user.password):
                return True

        return False


    def add(self, password):
        """ Add a new user
        Return:
            (result (boolean), errors (string))
        """
        self.db.open()
        return self.db.insert('INSERT INTO users (username,password) VALUES (?,?)', (self.user.username, generate_password_hash(self.user.password)))


    def remove(self):
        """ Remove a user
        Return:
            (result (boolean), errors (string))
        """
        self.db.open()
        return self.db.delete('DELETE FROM users WHERE username=?', (self.user.username,))


    def newPassword(self, newpwd):
        """ Update user password
        Params:
            username (string)
            newpwd (string) - New Password
        Return:
            (result (boolean), errors (string))
        """

        result = True
        error = ""

        self.db.open()
        result, error = self.db.update('UPDATE users SET password=? WHERE username=?', (generate_password_hash(newpwd), self.user.username))
        if not result:
            return (result, error)

        return (result, error)

    def getAll(self):
        """ Get all users in DB
        Return:
            users (Array[User])
        """
        users_list = []

        self.db.open()
        results = self.db.select('SELECT username, id FROM users', ())

        for result in results:
            tmp_user = User(username = result[0], id = result[1])
            users_list.append(tmp_user)

        return users_list


    def currentUser(self):
        user = load_user(self.user.username)
        return user
