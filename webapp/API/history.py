import logging,datetime

from webapp.API.Response import Response
from webapp.SessionsManager import Session, SessionsManager


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
                    "data": formatted_session_data,
                    "score": score,
                    "shots": shots,
                    "percentage": percentage
                }

                retrieved_sessions.append(formatted_session)
        
        retrieved_sessions.sort(reverse = True, key = lambda x: datetime.datetime.strptime(x['data'], '%d / %m / %y'))

        response.add("sessions", retrieved_sessions)

    except Exception as api_exception:
        response = Response(False)     
        logging.error("[history] API error - {}".format(api_exception))

    return response.compose()


