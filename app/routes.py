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

# Rota para fazer cadastro
@main.route('/get_user_register', methods=['POST', 'GET'])
def get_user_register():
    error_message = None

    if request.method == 'POST':
        name = request.form.get('name_register')
        email = request.form.get('email_register')
        password = request.form.get('password_register')


# Rota para fazer login
@main.route('/get_user_login', methods=['POST', 'GET'])
def get_user_login():
    error_message = None

    if request.method == 'POST':
        email = request.form.get('email_login')
        password = request.forml.get('password_login')
        