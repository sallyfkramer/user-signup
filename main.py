from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def index():
    return render_template('form.html')


def not_empty(x):
    if len(x) == 0:
        return False
    else:
        return True

def no_space(x):
    space = x.count(' ')
    if space == 0:
        return True
    else:
        return False

def valid_name(name):
    if len(name) >=3 and len(name) <= 20:
        return True
    else:
        return False

def contains(x):
    a = 0
    b = 0
    for c in x:
        if c=="@": 
            a+=1
    for f in x:
        if f=='.':
            b+=1
    if a==1 and b>=1:
        return True
                


@app.route('/', methods=['POST'])
def validate_input():
    name = request.form.get('name')
    password = request.form.get('password')
    again = request.form.get('again')
    email = request.form.get('email')

    name_error = ''
    password_error = ''
    email_error = ''

    if not not_empty(name):
        name_error = "User name cannot be blank."
    else:
        if not no_space(name):
            name_error = "User name cannot contain spaces."
        else:
            if valid_name(name) != True:
                name_error = "User name must be between 3 and 20 chararcters."

    if not not_empty(password):
        password_error = "Password cannot be blank."
    else:
        if not not_empty(again):
            password_error = "Please confirm password."
        else:
            if not no_space(password):
                password_error = "Password cannot contain spaces."
            else:
                if not valid_name(password):
                    password_error = "Password must be between 3 and 20 characters."
                else:
                    if not password==again:
                        password_error = "Passwords must match."

    if not no_space(email):
        email_error = "Not a valid email address."
    else:
        if not valid_name(email):
            email_error = "Not a valid email address."
        else:
            if not contains(email):
                email_error = "Not a valid email address."

    if len(email)==0:
        email_error = ''

    if not name_error and not password_error and not email_error:
        return redirect('/hello?name={0}'.format(name))
    else:
        return render_template('form.html', name = name, email = email, name_error = name_error, password_error = password_error, email_error = email_error)

@app.route("/hello")
def hello():
    name = request.args.get('name')
    return render_template('greeting.html', name = name)


app.run()