from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'cs490-summer'

admin = {"username":"admin", "password":"123"}

user1 = {"username":"test", "password":"test"}
user2 = {"username":"cs490", "password":"NJIT"}
user3 = {"username":"user", "password":"pass"}

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        if username == admin['username'] and password == admin['password']:
            session['user'] = username
            return redirect('/adminPage')
        
        if username == user1['username'] and password == user1['password']:
            session['user'] = username
            return redirect('/landing')

        if username == user2['username'] and password == user2['password']:
            session['user'] = username
            return redirect('/landing')
        
        if username == user3['username'] and password == user3['password']:
            session['user'] = username
            return redirect('/landing')

    return render_template("login.html")

@app.route('/register', methods=['POST', 'GET'])
def register():
    return render_template("register.html")

@app.route('/adminPage')
def adminPage():
    if('user' in session and session['user'] == admin['username']):
        return render_template("admin.html", name=admin['username'])

@app.route('/landing')
def landing():
    return render_template("landing.html")

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/home')


app.run(
    port=int(os.getenv('PORT',8080)),
    host=os.getenv('IP','0.0.0.0'),
    debug=True
    
    
)
