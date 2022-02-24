import logging,datetime

from webapp.API.Response import Response
from webapp.SessionsManager import Session, SessionsManager

def historyDataDelete(id_session, id_user):
    response = Response(True)
    
    try:
        sm = SessionsManager(id_user)
        sm.load(id_session)

        # Remove session
        result = sm.remove()

        if not result:
            response.status = False
            logging.error("[history delete] SessionManager error ")

    except Exception as api_exception:
        response.status = False   
        logging.error("[history delete] API error - {}".format(api_exception))

    return response.compose()

def historyDataEdit(id_session, id_user, date, shots):   
    response = Response(True)
    
    try:
        sm = SessionsManager(id_user)
        sm.load(id_session)

        # Check and load params
        session_data = datetime.datetime.strptime(date, '%d / %m / %y')
        sm.session.datetime = session_data.strftime('%d-%m-%y %H:%M:%S')
        
        shot_list = shots.split(",")
        for shot in shot_list:
            int(shot)

        sm.session.shots = "[" + shots + "]"
        
        sm.save()

    except Exception as api_exception:
        response = Response(False)     
        logging.error("[history edit] API error - {}".format(api_exception))

    return response.compose()


def historyDataRetrieve(id_user):
    response = Response(True)

    try:
        sm = SessionsManager(id_user)
        session_ids = sm.list()

        # Retrieve Sessions
        retrieved_sessions = []

        for id in session_ids:
            session = sm.load(id)

            if session != None:
                session_data = datetime.datetime.strptime(session.datetime, '%d-%m-%y %H:%M:%S')
                formatted_session_data = session_data.strftime('%d / %m / %y')

                session_scores_string = session.shots.replace("[","").replace("]","")
                session_scores = list(map(int, session_scores_string.split(",")))

                score = sum(session_scores)

                shots = len(session_scores)

                available_score = shots * 10
                percentage = (sum(session_scores) / available_score) * 100

                formatted_session = {
                    "id": session.id,
                    "data": formatted_session_data,
                    "score": score,
                    "shots": shots,
                    "shot_list": session_scores,
                    "percentage": percentage
                }

                retrieved_sessions.append(formatted_session)
        
        retrieved_sessions.sort(reverse = True, key = lambda x: datetime.datetime.strptime(x['data'], '%d / %m / %y'))

        response.add("sessions", retrieved_sessions)

    except Exception as api_exception:
        response = Response(False)     
        logging.error("[history retrieve] API error - {}".format(api_exception))

    return response.compose()


