from flask import Flask, render_template, request, redirect, url_for,session
from pymongo import MongoClient

app=Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['mt1']  
users_collection =  db['users']

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/methods')
def method():
    return render_template('methods.html')


@app.route('/dec')
def dec():
    return render_template('declarative.html')

@app.route('/ims')
def ims():
    return render_template('ims.html')

@app.route('/comprehension')
def comprehension():
    return render_template('comprehension.html')

@app.route('/conditional')
def condition():
    return render_template('conditional.html')

@app.route('/procedural')
def procedural():
    return render_template('procedural.html')

@app.route('/debugging')
def debug():
    return render_template('debugging.html')

@app.route('/planning')
def planning():
    return render_template('planning.html')

@app.route('/eval')
def eval():
    return render_template('eval.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users_collection.find_one({'username': username, 'password': password})
        if user:
            return redirect(url_for('home'))
        else:
            return render_template('login.html', message='Invalid username or password')
    return render_template('login.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        if users_collection.find_one({'username': username}):
            return render_template('register.html', message='Username already exists')
        else:
            users_collection.insert_one({'username': username, 'password': password, 'email': email})
            return redirect(url_for('home'))
    return render_template('register.html')



@app.route('/home')
def index():
    return render_template('home.html')



@app.route('/home')
def home():
    return render_template('home.html')



@app.route('/technique')
def technique_for():
    return render_template('technique.html')



@app.route('/logout')
def logout():
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
