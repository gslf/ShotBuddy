from webapp.Session import Session

def SessionsManager():
    """A class to manage sessions

    Attributes:
        session - (Session) Current managed session
    """

    def __init__(self, session = None):
        self.session = session


    def list(self):
        """List all session for the current user
        
        Return:
            sessions - [int] A list of session ID's
        """
        #TODO
        pass

    def load(self, session_id):
        """Load a specific session from DB for the current user

        Params:
            session_id - (int) Session ID

        Return:
            self.session (Session)
        """
        #TODO
        pass

    
    def loadLast(self):
        """Load the last session from DB for the curent user

        Return:
            self.session (Session)
        """
        #TODO
        pass

    def save(self):
        """Save current session to the DB

        Return
            result - (boolean) The DB writing result
        """
        #TODO
        pass

    def remove(self):
        """Delete current session from the DB

        Return
            result - (boolean) The DB writing result
        """
        #TODO
        pass