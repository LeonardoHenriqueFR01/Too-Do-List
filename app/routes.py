from flask import render_template, request, redirect, url_for, session, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User
from time import sleep


main = Blueprint('main', __name__)

# Rota para página principal
@main.route('/')
def index():
    return render_template('index.html')

# Rota para página apos fazer cadastro ou login
@main.route('/home')
def home():
    return render_template('home.html')

# Rota para fazer registro
@main.route('/get_user_register', methods=['POST', 'GET'])
def get_user_register():
    error_message = None

    if request.method == 'POST':
        name = request.form.get('name_register')
        email = request.form.get('email_register')
        password = request.form.get('password_register')

        user_exists = User.query.filter((User.name == name) | (User.email == email)).first()

        if user_exists:
            error_message = 'Nome ou Email já cadastrado!'
            return render_template('index.html', error_register=error_message)

        else:
            hash_password = generate_password_hash(password)

            user = User(name=name, email=email, password=hash_password)

            db.session.add(user)
            db.session.commit()

            sleep(2)

            return redirect(url_for('main.home'))
    
    return render_template('index.html')


# Rota para fazer login
@main.route('/get_user_login', methods=['POST', 'GET'])
def get_user_login():
    error_message = None

    if request.method == 'POST':
        email = request.form.get('email_login')
        password = request.form.get('password_login')
        
        user_exists = User.query.filter((User.email == email)).first()

        if user_exists and check_password_hash(user_exists.password, password):
            sleep(3)

            return redirect(url_for('main.home'))
        else:
            error_message = 'Dados inválidos!'
            return render_template('index.html', error_login=error_message)

    return render_template('index.html')    
