from flask import Flask, render_template, request, redirect
import random
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        valeur_max = int(request.form['valeurMax']) 
        valeur_a_afficher =random.randint(1, valeur_max)
        return render_template('home.html', valeur_max=valeur_max,valeur_a_afficher = valeur_a_afficher)
       
    else:
        return redirect('/')

