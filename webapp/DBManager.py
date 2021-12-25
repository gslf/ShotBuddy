import sqlite3 as sql
from webapp.vars import SQL_DB


class DBManager():
    """ SQLite3 DB Management Interface
    Attributes:
        db      Database object
        cursor  Database cursor
    """

    def __init__(self):
        self.db = None
        self.cursor = None


    def open(self):
        """ Open a new DB connection
        """
        self.db = sql.connect(SQL_DB)
        self.cursor = self.db.cursor()


    def insert(self, query, values):
        """ Insert a new row
        Params
            query(string)   Insert query
            value(tuple)    Insert query parameter
        Return
            (result (id), Error (string))
        """
        try:
            self.cursor.execute(query, values)
            self.db.commit()
            return (self.cursor.lastrowid, "")
        except sql.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        except Exception as error:
            self.db.close()
            return(False, "Query Failed! Error:{}".format(str(error)))
        finally:
            self.db.close()


    def select(self, query, values):
        """ Select rows by parameter
        Params
            query(string)   Select query
            value(tuple)    Select query parameter
        Return
            selected rows
        """
        try:
            self.cursor.execute(query, values)
            return self.cursor.fetchall()
        except Exception as error:
            self.db.close()
            return []
        finally:
            self.db.close()


    def delete(self, query, values):
        """ Delete a row
        Params
            query(string)   Delete query
            value(tuple)    Delete query parameter
        Return
            (result (boolean), Error (string))
        """
        try:
            self.cursor.execute(query, values)
            self.db.commit()
            return (True, "")
        except Exception as error:
            self.db.close()
            return (False, "Query Failed! Error:{}".format(str(error)))
        finally:
            self.db.close()


    def update(self, query, values):
        """ Update a row
        Params
            query(string)   Update query
            value(tuple)    Update query parameter
        Return
            (result (boolean), Error (string))
        """
        try:
            self.cursor.execute(query, values)
            self.db.commit()
            return (True, "")
        except Exception as error:
            self.db.close()
            return (False, "Query Failed! Error:{}".format(str(error)))
        finally:
            self.db.close()


    def close(self):
        """ Close DB connection
        """
        self.db.close()

        