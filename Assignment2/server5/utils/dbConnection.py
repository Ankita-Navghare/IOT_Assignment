import mysql.connector

def getDBConnection():
    connection = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        database = "iotdb",
        use_pure = True
    )
    return connection