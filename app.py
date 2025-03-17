from flask import Flask, render_template
from config import Config
from extensions import db, migrate
from models import student
import services.students_actions as st_act
 
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students')
def students():
    return render_template('students.html', students=st_act.view_students())

@app.route('/create', methods=['GET', 'POST'])
def create():
    return

if __name__ == "__main__":
    app.run(debug=True)