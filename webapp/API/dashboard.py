import logging, datetime
from webapp.API.Response import Response
from webapp.SessionsManager import Session, SessionsManager


def dashboardDataRetrieve(id_user):
    response = Response(True)

    try: 
        sm = SessionsManager(id_user)
        session_ids = sm.list()

        #Retrieve latest 6 sessions
        retrieved_sessions = []
        for id in session_ids[-30:]:
            result = sm.load(id)

            if result != None:
                retrieved_sessions.append(result)
            
        # Stats Data
        # Last session data
        session_data = datetime.datetime.strptime(retrieved_sessions[-1].datetime, '%d-%m-%y %H:%M:%S')
        response.add("session_data", session_data.strftime('%d / %m / %y'))

        # Last session scored points
        last_session_scores_string = retrieved_sessions[-1].shots.replace("[","").replace("]","")
        last_session_scores = list(map(int, last_session_scores_string.split(",")))
        response.add("last_session_score", sum(last_session_scores))

        # Last session total points
        last_session_total = len(last_session_scores) * 10
        response.add("last_session_total", last_session_total)

        # Last session percentage
        last_session_percent = (sum(last_session_scores) / last_session_total) * 100
        response.add("last_session_percent", last_session_percent)

        # Average 5 session percentage
        sessions_scores = []
        for session in retrieved_sessions[-5: ]:
            scores_string = session.shots.replace("[","").replace("]","")
            scores = list(map(int, scores_string.split(",")))
            sessions_scores = sessions_scores + scores

        session_percent = (sum(sessions_scores) / (len(sessions_scores) * 10)) * 100
        response.add("session_tot_percent_5", session_percent)
        
        # Average 10 sessions percentage
        for session in retrieved_sessions[-10: -6]:
            scores_string = session.shots.replace("[","").replace("]","")
            scores = list(map(int, scores_string.split(",")))
            sessions_scores = sessions_scores + scores

        session_percent = (sum(sessions_scores) / (len(sessions_scores) * 10)) * 100
        response.add("session_tot_percent_10", session_percent)

        # Average 20 session percentage
        for session in retrieved_sessions[-20: -11]:
            scores_string = session.shots.replace("[","").replace("]","")
            scores = list(map(int, scores_string.split(",")))
            sessions_scores = sessions_scores + scores

        session_percent = (sum(sessions_scores) / (len(sessions_scores) * 10)) * 100
        response.add("session_tot_percent_20", session_percent)

        # Average 30 session percentage
        for session in retrieved_sessions[-30: -21]:
            scores_string = session.shots.replace("[","").replace("]","")
            scores = list(map(int, scores_string.split(",")))
            sessions_scores = sessions_scores + scores

        session_percent = (sum(sessions_scores) / (len(sessions_scores) * 10)) * 100
        response.add("session_tot_percent_30", session_percent)

        # Charts Data
        # Array with last 10 session percentage
        session_percent_10 = []

        #Array with last 10 session scored points
        scored_point_10 = []

        # Array with last 10 session shoted points
        shooted_points_10 = []

        # Array with last 10 session ERRORS (difference betweet scored percentage and target percentage)
        errors_10 = []

        for session in retrieved_sessions[-10:]:
            scores_string = session.shots.replace("[","").replace("]","")
            scores = list(map(int, scores_string.split(",")))
            percentage = (sum(scores) / (len(scores) * 10)) * 100

            session_percent_10.append(percentage)

            scored_point_10.append(sum(scores))

            shooted_points_10.append(len(scores) * 10)

            errors_10.append(percentage - session.percentage_target)

        response.add("session_percentage_10", session_percent_10)
        response.add("scored_point_10", scored_point_10)
        response.add("shooted_points_10", shooted_points_10)
        response.add("errors_10", errors_10)


        
    except Exception as api_exception:
        response = Response(False)     
        logging.error("[dashboard] API error - {}".format(api_exception))

    return response.compose()