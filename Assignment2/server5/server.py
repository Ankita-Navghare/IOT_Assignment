from flask import Flask, request
from utils.createResponse import createResponse
from utils.executeSelectQuery import executeSelectQuery
from utils.executeQuery import executeQuery

server = Flask(__name__)


@server.route('/', methods=['GET'])
def homepage():
    return createResponse("Fitness Tracker IoT Application")


@server.route('/add', methods=['POST'])
def add_user():
    data = request.form if request.form else request.get_json()

    query = f"""
    INSERT INTO fitness_users(name, age, city, steps, pulse, spo2, temperature)
    VALUES(
        '{data.get("name")}',
        {data.get("age")},
        '{data.get("city")}',
        {data.get("steps")},
        {data.get("pulse")},
        {data.get("spo2")},
        {data.get("temperature")}
    );
    """
    executeQuery(query)
    return createResponse("add : success")


@server.route('/all', methods=['GET'])
def get_all_users():
    query = "SELECT * FROM fitness_users;"
    values = executeSelectQuery(query)
    return createResponse(values)

@server.route('/info', methods=['POST'])
def get_single_user():
    data = request.form if request.form else request.get_json()
    name = data.get("name")

    query = f"SELECT * FROM fitness_users WHERE name = '{name}';"
    values = executeSelectQuery(query)
    return createResponse(values)


@server.route('/update', methods=['PUT', 'POST'])
def update_city():
    data = request.form if request.form else request.get_json()

    query = f"""
    UPDATE fitness_users
    SET city = '{data.get("city")}'
    WHERE name = '{data.get("name")}';
    """
    executeQuery(query)
    return createResponse("update : success")


@server.route('/steps', methods=['GET'])
def max_steps():
    query = """
    SELECT * FROM fitness_users
    WHERE steps = (SELECT MAX(steps) FROM fitness_users);
    """
    values = executeSelectQuery(query)
    return createResponse(values)


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=5000, debug=True)
