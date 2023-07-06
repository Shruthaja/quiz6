import pyodbc as pyodbc
from flask import Flask, render_template, request, session

from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

server = 'assignmnet6.database.windows.net'
database = 'testDB'
username = 'shruthaja'
password = 'mattu4-12'
driver = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')
cursor = conn.cursor()

d = {}


@app.route('/', methods=['GET', 'POST'])
def home():
    score = 0
    username = ''
    if request.method == "POST":
        pname1 = request.form['player1']
        session['name'] = pname1
        print(session)
        # pile2 = int(request.form['player2pile']) - 1
        query = "insert into play values(?,0)"
        cursor.execute(query, pname1)
        cursor.commit()
        query = "select score from play where player=?"
        cursor.execute(query, pname1)
        score = cursor.fetchone()
        return render_template("game.html", username=pname1, score=score[0])
    return render_template("index.html")


@app.route('/game', methods=['GET', 'POST'])
def game():
    correct = ""
    username = ''
    global d
    if request.method == "POST":
        qno = request.form['question']
        ans = request.form['answer']
        name = request.form['name']
        query = "select score from play"
        cursor.execute(query)
        score = cursor.fetchone()
        if (qno == 'q1'):
            if (ans == '2'):
                correct = 'ok'
                f = open('result', 'a')
                f.write("{" + name + ":q1}\n")
                return render_template("game.html", correct=correct, username=name)
        if (qno == 'q2'):
            if (ans == '100'):
                correct = 'ok'
                f = open('result', 'a')
                f.write("{" + name + ":q2}\n")
                return render_template("game.html", correct=correct, username=name)
        if (qno == 'q3'):
            if (ans == '300'):
                correct = 'ok'
                f = open('result', 'a')
                f.write("{" + name + ":q3}\n")
                return render_template("game.html", correct=correct, username=name)
        else:
            correct = 'NO'
            return render_template("game.html", correct=correct, username=name)
    return render_template("game.html", correct="")


@app.route('/judge', methods=['GET', 'POST'])
def judge():
    result = []
    if request.method == "POST":
        query = "truncate table play;"
        cursor.execute(query).commit()
        f = open("result", 'w')
        f.write("")
        return render_template("judge.html", result=result)
    f1 = open('result', 'r').read()
    f1 = f1.split()
    return render_template("judge.html", result=f1)


if __name__ == '__main__':
    app.run(debug=True)
