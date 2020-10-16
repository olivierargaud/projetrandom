from flask import Flask, url_for , request , render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'do_the_login() POST'
    else:
        return 'show_the_login_form() GET'


with app.test_request_context():
    print(url_for('static', filename='style.css'))

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
    