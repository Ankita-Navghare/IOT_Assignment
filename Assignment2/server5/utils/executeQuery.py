from utils.dbConnection import getDBConnection

def executeQuery(query):
    # get connection with mysql server
    connection = getDBConnection()

    # create a cursor to execute a query
    cursor = connection.cursor()

    # execute query with cursor
    cursor.execute(query)

    # commit change to database server
    connection.commit()

    # close the cursor
    cursor.close()

    # close the connection
    connection.close()