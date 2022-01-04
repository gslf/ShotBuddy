import logging
from webapp.API.Response import Response
from webapp.SessionsManager import Session, SessionsManager

def dashboardDataRetrieve(id_user):
    response = Response(True)

    try: 
        sm = SessionsManager(id_user)
        session_ids = sm.list()

        #Retrieve latest 6 sessions
        retrieved_sessions = []
        for id in session_ids[-6:]:
            result = sm.load(id)

            if result != None:
                retrieved_sessions.append(result)
            
        # TODO Stats Data
        # Last session data
        # Last session scored points
        # Last session total points
        # Last session percentage
        # Average 5 session percentage
        # Average 10 sessions percentage
        # Average 20 session percentage
        # Average 30 session percentage

        # TODO Charts Data
        # Array with last 6 session percentage
        # Array with last 6 session scored points
        # Array with last 6 session shoted points
        # Array with last 6 session ERRORS (difference betweet scored percentage and target percentage)

        pass
        
    except Exception as api_exception:
        response = Response(False)     
        logging.error("[dashboard] API error - {}".format(api_exception))

    return response.compose()