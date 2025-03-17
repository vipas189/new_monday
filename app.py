from flask import Flask, render_template
from config import Config
from extensions import db, migrate
from models import student
 
app = Flask(__name__)
app.config.from_object(config_class=Config)

db.init_app(app)
migrate.init_app(app, db) 

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)