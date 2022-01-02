import logging
from webapp.API.Response import Response

def dashboardDataRetrieve(id_user):
    response = Response(True)

    try: 
        print(id_user)
        
    except Exception as api_exception:
        response = Response(False)     
        logging.error("[dashboard] API error - {}".format(api_exception))

    return response.compose()