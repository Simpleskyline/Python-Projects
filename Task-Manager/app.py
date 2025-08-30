<<<<<<< HEAD
#import
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#create flask app
app = Flask(__name__)

#set the database to a SQLite file named test.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

#connect SQLAchemy to the flask app
db = SQLAlchemy(app)

#3. Database Model (Table definition)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Task {self.id}>'

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        task_content = request.form['content'] #gets the task content
        new_task = Todo(content=task_content) #creates a new Todo object

        try:
            db.session.add(new_task) #adds it to the database
            db.session.commit() #saves it
            return redirect('/') #redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all() #fetches all tasks from database
        return render_template("index.html", tasks=tasks)  # pass tasks to template


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('update.html', task=task)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
=======
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"]) 
def calculator():
    result = None
    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operator = request.form["operator"]

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2 if num2 != 0 else "Error! Division by zero"
        elif operator == "**":
            result = num1 ** num2
        elif operator == "%":
            result = num1 % num2

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> repoB-branch
