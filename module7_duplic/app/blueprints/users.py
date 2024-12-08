from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app.db_connect import get_db

users_bp = Blueprint('users', __name__)

from werkzeug.security import check_password_hash


@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = get_db().cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user and check_password_hash(user['password_hash'], password):
            session['user'] = {'id': user['id'], 'email': user['email']}
            return redirect(url_for('profile'))  # Redirect to profile after login
        flash("Invalid email or password.", "danger")
    return render_template('login.html')


@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        connection = get_db()
        cursor = connection.cursor()

        # Check if the email is already registered
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('Email already registered. Please log in.', 'danger')
            return redirect(url_for('users.login'))

        # Hash the password and insert into the database
        hashed_password = generate_password_hash(password)
        cursor.execute("INSERT INTO users (email, password_hash) VALUES (%s, %s)", (email, hashed_password))
        connection.commit()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('users.login'))

    return render_template('register.html')

@users_bp.route('/profile')
def profile():
    if 'user_id' not in session:
        flash('You must be logged in to view this page.', 'warning')
        return redirect(url_for('users.login'))

    user_id = session['user_id']
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    user = cursor.fetchone()
    return render_template('profile.html', user=user)

@users_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash("You have been logged out.", "success")
    return redirect(url_for('login'))






