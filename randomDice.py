from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import random



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///baseRandomDice.db'
db = SQLAlchemy(app)


valeur_max = 1
valeur_a_afficher = 0





class dice(db.Model):
""" table qui definit les dés """
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    value = db.Column(db.Integer, nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Dé %r %r>' % (self.name , self.value)


class dice_group(db.Model):
""" table qui definit les groupe de dés (lancer plusieurs dés) """
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    children = db.relationship("dice_list_group")

    def __repr__(self):
        return '<groupe %r>' % (self.name)


class dice_list_group(db.Model):
""" table de liaison entre les dés et les groupes de dés """
    id = db.Column(db.Integer, primary_key = True)
    idDice = db.Column(db.Integer)
    idGroup = db.Column(db.Integer, ForeignKey('dice_group.id'))
    
    def __repr__(self):
        return '<idDice %r %r>' % (self.idDice , self.idGroup)




class user(db.Model):
""" table qui definit les utilisateurs """
    login = db.Column(db.String(200), nullable = False , primary_key = True)
    mdp = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)


    def __repr__(self):
        return '<User %r >' % self.name 






@app.route('/')
def hello_world():
    return render_template('login.html')

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

@app.route('/login',methods=['POST'])
def login():
    if request.method == 'POST':
        print (request.form['login'])
        print (request.form['mdp'])
        return render_template('home.html', valeur_max=valeur_max,valeur_a_afficher = valeur_a_afficher)
       
    else:
        return redirect('/')

@app.route('/logout',methods=['POST','GET'])
def logout():
    if request.method == 'POST':
       
        return render_template('login.html')
       
    else:
        return redirect('/')

@app.route('/nouveauCompte')
def nouveauCompteDeBase():
   
    return render_template('nouveauCompte.html')

@app.route('/nouveauCompte',methods=['POST'])
def nouveauCompte():
    if request.method == 'POST':
        return render_template('nouveauCompte.html', valeur_max=valeur_max,valeur_a_afficher = valeur_a_afficher)
       
    else:
        return redirect('/')

@app.route('/validerNouveauCompte',methods=['POST'])
def validerNouveauCompte():
    
    print (request.form['login'])
    print (request.form['mdp'])

    loginSaisie = request.form['login']
    mdpSaisie = request.form['mdp']

    new_user = user(login=loginSaisie,mdp = mdpSaisie)

    try:
            db.session.add(new_user)
            db.session.commit()
            return render_template('home.html')

    except:
        return redirect('/nouveauCompte')



       
   