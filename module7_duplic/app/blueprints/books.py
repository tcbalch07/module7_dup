from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.db_connect import get_db

books_bp = Blueprint('books', __name__)

@books_bp.route('/catalog')
def catalog():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    return render_template('catalog.html', books=books)

@books_bp.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        price = request.form['price']

        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO books (title, author, price) VALUES (%s, %s, %s)", (title, author, price))
        db.commit()
        flash('Book added successfully!')
        return redirect(url_for('books.catalog'))
    return render_template('add_book.html')

@books_bp.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        price = request.form['price']

        cursor.execute("UPDATE books SET title=%s, author=%s, price=%s WHERE books_id=%s", (title, author, price, book_id))
        db.commit()
        flash('Book updated successfully!')
        return redirect(url_for('books.catalog'))

    cursor.execute("SELECT * FROM books WHERE books_id=%s", (book_id,))
    book = cursor.fetchone()
    return render_template('edit_book.html', book=book)

@books_bp.route('/delete/<int:book_id>')
def delete_book(book_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM books WHERE books_id=%s", (book_id,))
    db.commit()
    flash('Book deleted successfully!')
    return redirect(url_for('books.catalog'))







