# import Flask
from flask import Flask, request
import mysql.connector

# create server
app = Flask(__name__)

@app.get('/')
def homepage():
    return "This is home page"

# ================= GET ALL EMPLOYEES =================
@app.route('/employees', methods=['GET'])
def get_employees():
    conn = mysql.connector.connect(
        host='localhost',
        port=3306,
        user="root",
        password="root",
        database="iotdb",
        use_pure=True
    )
    cursor = conn.cursor()
    cursor.execute("select * from employees;")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"employees": data}

# ================= ADD EMPLOYEE =================
@app.route('/employee', methods=['POST'])
def post_employee():
    data = request.form if request.form else request.get_json()

    empid = data.get('empid')
    name = data.get('name')
    department = data.get('department')
    email = data.get('email')
    salary = data.get('salary')
    doj = data.get('doj')

    conn = mysql.connector.connect(
        host='localhost',
        port=3306,
        user="root",
        password="root",
        database="iotdb",
        use_pure=True
    )
    query = f"""
    insert into employees
    values({empid}, '{name}', '{department}', '{email}', {salary}, '{doj}');
    """
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "Employee added successfully"}

# ================= UPDATE EMPLOYEE =================
@app.route('/employee', methods=['PUT'])
def update_employee():
    data = request.form if request.form else request.get_json()

    empid = data.get('empid')
    department = data.get('department')

    conn = mysql.connector.connect(
        host='localhost',
        port=3306,
        user="root",
        password="root",
        database="iotdb",
        use_pure=True
    )
    query = f"update employees set department='{department}' where empid={empid};"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "Employee updated successfully"}

# ================= DELETE EMPLOYEE =================
@app.route('/employee', methods=['DELETE'])
def delete_employee():
    data = request.form if request.form else request.get_json()

    empid = data.get('empid')

    conn = mysql.connector.connect(
        host='localhost',
        port=3306,
        user="root",
        password="root",
        database="iotdb",
        use_pure=True
    )
    query = f"delete from employees where empid={empid};"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "Employee deleted successfully"}

# ================= EMPLOYEES BY DEPARTMENT =================
@app.route('/employees/department', methods=['POST'])
def department_employees():
    data = request.form if request.form else request.get_json()
    department = data.get('department')

    conn = mysql.connector.connect(
        host='localhost',
        port=3306,
        user="root",
        password="root",
        database="iotdb",
        use_pure=True
    )
    query = f"select * from employees where department='{department}';"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    return {"employees": result}

# ================= HIGHEST SALARY =================
@app.route('/employee/highest', methods=['GET'])
def highest_salary():
    conn = mysql.connector.connect(
        host='localhost',
        port=3306,
        user="root",
        password="root",
        database="iotdb",
        use_pure=True
    )
    cursor = conn.cursor()
    cursor.execute("select * from employees order by salary desc limit 1;")
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    return {"highest_salary_employee": result}

# ================= LOWEST SALARY =================
@app.route('/employee/lowest', methods=['GET'])
def lowest_salary():
    conn = mysql.connector.connect(
        host='localhost',
        port=3306,
        user="root",
        password="root",
        database="iotdb",
        use_pure=True
    )
    cursor = conn.cursor()
    cursor.execute("select * from employees order by salary asc limit 1;")
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    return {"lowest_salary_employee": result}

# run server
if __name__ == '__main__':
    app.run(debug=True)
