from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)




valeur_max = 1
valeur_a_afficher = 0



class Dice(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    value = db.Column(db.Integer, nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)


    def __repr__(self):
        return '<Dé %r %r>' % (self.name , self.value)





@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        valeur_max = int(request.form['valeurMax']) 
        print ('valeur maximum')
        print (valeur_max)
        return render_template('home.html', valeur_max=valeur_max,valeur_a_afficher = valeur_a_afficher)
       
    else:
        return redirect('/')

@app.route('/lancer',methods=['POST','GET'])
def lancerDe():
    if request.method == 'POST':
        valeur_a_afficher =random.randint(1, valeur_max)
        print ('valeur maximum')
        print (valeur_max)
        return render_template('home.html', valeur_max=valeur_max,valeur_a_afficher = valeur_a_afficher)
       
    else:
        return redirect('/')

