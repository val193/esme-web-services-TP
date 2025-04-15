from flask import Blueprint, request, jsonify
from models import db, Book, Student, StudentBook #on rajoute Student et StudentBook
from datetime import datetime

books_bp = Blueprint('books', __name__)

# 🔹 Récupérer tous les livres
@books_bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([
        {'id': b.id, 'title': b.title, 'author': b.author, 'published_at': b.published_at.strftime('%Y-%m-%d') if b.published_at else None}
        for b in books
    ])

# 🔹 Récupérer un livre par ID
@books_bp.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify({
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'published_at': book.published_at.strftime('%Y-%m-%d') if book.published_at else None
    })

# 🔹 Ajouter un livre
@books_bp.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()

    if not data or 'title' not in data or 'author' not in data:
        return jsonify({'error': 'Invalid data, title and author are required'}), 400

    published_at = None
    if 'published_at' in data:
        try:
            published_at = datetime.strptime(data['published_at'], '%Y-%m-%d')
        except ValueError:
            return jsonify({'error': 'Invalid date format, expected YYYY-MM-DD'}), 400

    book = Book(title=data['title'], author=data['author'], published_at=published_at)
    db.session.add(book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully', 'id': book.id}), 201

# 🔹 Mettre à jour un livre
@books_bp.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    if 'title' in data:
        book.title = data['title']
    if 'author' in data:
        book.author = data['author']
    if 'published_at' in data:
        try:
            book.published_at = datetime.strptime(data['published_at'], '%Y-%m-%d')
        except ValueError:
            return jsonify({'error': 'Invalid date format, expected YYYY-MM-DD'}), 400

    db.session.commit()
    return jsonify({'message': 'Book updated successfully'})

# 🔹 Supprimer un livre
@books_bp.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})

# 🔹 Emprunter un livre
@books_bp.route('/books/<int:book_id>/borrow', methods=['POST'])
def borrow_book(book_id):

    #on récupère l'id de l'étudiant qui veut emprunter le livre 
    data = request.get_json()
    student_id = data.get('student_id')
    student = Student.query.get(student_id)

    book = Book.query.get(book_id)

    if not student or not book:
        return jsonify({'error': 'Student or Book not found'}), 404

    #on vérifie si ce livre est déjà emprunté
    existing_borrow = StudentBook.query.filter_by(book_id=book_id, return_date=None).first()
    if existing_borrow:
        return jsonify({'error': 'Book is already borrowed'}), 400

    #on update StudentBook
    borrow = StudentBook(
        student_id=student_id,
        book_id=book_id,
        borrow_date=datetime.now() #date locale 
    )
    db.session.add(borrow)
    db.session.commit()

    return jsonify({'message': 'Book borrowed successfully'})

# 🔹 Rendre un livre
@books_bp.route('/books/<int:book_id>/return', methods=['POST'])
def return_book(book_id):
    data = request.get_json()
    student_id = data.get('student_id')

    borrow = StudentBook.query.filter_by(book_id=book_id, student_id=student_id, return_date=None).first()

    if not borrow:
        return jsonify({'error': 'This student has not borrowed this book or already returned it'}), 404

    borrow.return_date = datetime.now()
    db.session.commit()

    return jsonify({'message': 'Book returned successfully'})
