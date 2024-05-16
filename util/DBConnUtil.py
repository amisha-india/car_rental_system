# Putting all connection separetly because of the open and close problem of connection for each object

import pyodbc #python open database connection
from util.PropertyUtil import PropertyUtil

class DBConnUtil:
    conn = None
    @staticmethod
    def getConnection():
        if DBConnUtil.conn is None:
            connectionString = PropertyUtil.get_property_string()
            try:
                DBConnUtil.conn = pyodbc.connect(connectionString)
            except ConnectionError as e:
                print(f"Failed to establish connection: {e}")
        else:
            print("Connection already established")
        return DBConnUtil.conn
        
    @staticmethod
    def closeConnection():
        if DBConnUtil.conn is not None:
            DBConnUtil.conn.close()
            DBConnUtil.conn = None
        
        else:
            print("No such connection exists")
        return DBConnUtil.conn

