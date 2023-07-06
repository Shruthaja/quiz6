import pyodbc as pyodbc
from flask import Flask, render_template, request

app = Flask(__name__)
server = 'assignmnet6.database.windows.net'
database = 'testDB'
username = 'shruthaja'
password = 'mattu4-12'
driver = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')
cursor = conn.cursor()


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
