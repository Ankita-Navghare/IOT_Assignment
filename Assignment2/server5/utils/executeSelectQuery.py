from utils.dbConnection import getDBConnection

def executeSelectQuery(query):
    # get connection with mysql server
    connection = getDBConnection()

    # create a cursor to execute a query
    cursor = connection.cursor()

    # execute query with cursor
    cursor.execute(query)

    # get data from cursor
    data = cursor.fetchall()

    # close the cursor
    cursor.close()

    # close the connection
    connection.close()

    # return data
    return data