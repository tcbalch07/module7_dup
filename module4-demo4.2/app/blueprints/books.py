from flask import Blueprint, render_template, request, url_for, redirect, flash
from app.db_connect import get_db

# Add a unique name for the blueprint to avoid conflicts.

books = Blueprint('books_blueprint', __name__, url_prefix='/books')

@books.route('/book', methods=['GET', 'POST'])
def book():
    db = get_db()
    cursor = db.cursor()

    # Handle POST request to add a new book
    if request.method == 'POST':
        book_name = request.form['book_name']
        genre = request.form['genre']

        # Insert the new book into the database
        cursor.execute('INSERT INTO books (book_name, genre) VALUES (%s, %s)', (book_name, genre))
        db.commit()

        flash('New book added successfully!', 'success')
        return redirect(url_for('books.book'))

    # Handle GET request to display all books
    cursor.execute('SELECT * FROM books')
    all_books = cursor.fetchall()
    return render_template('books.html', all_books=all_books)


@books.route('/update_book/<int:book_id>', methods=['GET', 'POST'])
def update_book(book_id):
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        # Update the book's details
        book_name = request.form['book_name']
        genre = request.form['genre']

        cursor.execute('UPDATE books SET book_name = %s, genre = %s WHERE book_id = %s',
                       (book_name, genre, book_id))
        db.commit()

        flash('Book updated successfully!', 'success')
        return redirect(url_for('books.book'))

    # GET method: fetch book's current data for pre-populating the form
    cursor.execute('SELECT * FROM books WHERE book_id = %s', (book_id,))
    book = cursor.fetchone()
    return render_template('update_book.html', book=book)

@books.route('/delete_book/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    db = get_db()
    cursor = db.cursor()

    # Delete the book
    cursor.execute('DELETE FROM books WHERE book_id = %s', (book_id,))
    db.commit()

    flash('Book deleted successfully!', 'danger')
    return redirect(url_for('books.book'))

@books.route('/suggest_books', methods=['GET', 'POST'])
def suggest_books():
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        book_name = request.form['book_name']
        genre = request.form['genre']

        # Insert the new book suggestion into the database
        cursor.execute('INSERT INTO books (book_name, genre) VALUES (%s, %s)', (book_name, genre))
        db.commit()

        flash('Your book suggestion has been submitted!', 'success')
        return redirect(url_for('books.suggest_books'))

    return render_template('suggest_books.html')
