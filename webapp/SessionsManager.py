from webapp.DBManager import DBManager
from webapp.Session import Session

class SessionsManager():
    """A class to manage sessions

    Attributes:
        current_user_id - (int) The ID of the current user
        session - (Session) Current managed session
    """

    def __init__(self, current_user_id, session=None):
        self.current_user_id = current_user_id
        self.session = session

        self.db = DBManager()


    def list(self):
        """List all session for the current user
        
        Return:
            sessions - [int] A list of session ID's
        """
        # Retrieve all session for the current user
        self.db.open()
        results = self.db.select('SELECT * FROM sessions WHERE id_user=?', (self.current_user_id,))
        self.db.close()

        sessions_ids = []
        for result in results:
            sessions_ids.append(result[0])
        
        return sessions_ids

    def load(self, session_id):
        """Load a specific session from DB for the current user

        Params:
            session_id - (int) Session ID

        Return:
            self.session (Session)
        """
        self.db.open()
        results = self.db.select('SELECT * FROM sessions WHERE id=?', (session_id,))
        self.db.close()

        if results != None and len(results) > 0:
            retrieved_session = results[0]

            self.session = Session(
                id_user = retrieved_session[1],
                datetime = retrieved_session[2],
                percentage_target = retrieved_session[3],
                shots = retrieved_session[4],
                duration = retrieved_session[5],
                id = retrieved_session[0]
            )

        else:
            self.session = None
        
        return self.session

    
    def loadLast(self):
        """Load the last session from DB for the curent user

        Return:
            self.session (Session)
        """
        sessions_ids = self.list()
        
        if len(sessions_ids) > 0:
            last_id = sessions_ids[-1]
            _ = self.load(last_id)
        else:
            self.session = None

        return self.session

    def new(self, id_user, datetime, percentage_target, shots, duration):
        """Create a new session and save it to the DB

        Return:
            result - (boolean) The new session creation result
        """
        self.session = Session(
            id_user = id_user,
            datetime = datetime,
            percentage_target = percentage_target,
            shots = shots,
            duration = duration
        )

        self.db.open()
        new_id, errors = self.db.insert('INSERT INTO sessions (id_user, datetime, percentage_target, shots, duration) VALUES (?,?,?,?,?)', (id_user, datetime, percentage_target, shots, duration))
        self.db.close()

        if new_id != False:
            self.session.id = new_id
            return True
        else:
            print(errors)
            return False


    def save(self):
        """Save current session to the DB

        Return
            result - (boolean) The DB writing result
        """

        if self.session != None and self.session.id > 0:
            self.db.open()
            result, errors = self.db.update('UPDATE sessions SET id_user=?, datetime = ?, percentage_target=?, shots=?, duration=? WHERE id=?', (
                self.session.id_user, self.session.datetime, self.session.percentage_target, self.session.shots, self.session.duration, self.session.id))
            self.db.close()

            if result:
                return True
            else:
                print(errors)
                return False
        else:
            return False
        

    def remove(self):
        """Delete current session from the DB

        Return
            result - (boolean) The DB writing result
        """

        self.db.open()
        result = self.db.delete('DELETE FROM sessions WHERE id=?', (self.session.id,))
        self.db.open()

        if result:
            self.session = None
            return True
        else:
            return False