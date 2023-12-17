import pytest
from pydantic import ValidationError


from app.api.models import BookIn, BookOut, BookUpdate

book = BookIn(book_title='Title',
              book_description='Desc',
              book_genres=['G1'],
              authors_id=[1],)

def test_create_book(book:BookIn=book):
    assert dict(book) == {'book_title':book.book_title,
                          'book_description':book.book_description,
                          'book_genres':book.book_genres,
                          'authors_id':book.authors_id,}

def test_update_book_title(book:BookIn=book):
    book_upd = BookOut(
        book_title='New Title',
        book_description=book.book_description,
        book_genres=book.book_genres,
        authors_id=book.authors_id,
        id = 1
    )
    assert dict(book_upd) == {'book_title':book_upd.book_title,
                        'book_description':book_upd.book_description,
                        'book_genres':book_upd.book_genres,
                        'authors_id':book_upd.authors_id,
                        'id': book_upd.id}

def test_update_book_genre(book:BookIn=book):
    book_upd = BookOut(
        book_title=book.book_title,
        book_description=book.book_description,
        book_genres=['Genre 1', 'Genre 2'],
        authors_id=book.authors_id,
        id = 1
    )
    assert dict(book_upd) == {'book_title':book_upd.book_title,
                        'book_description':book_upd.book_description,
                        'book_genres':book_upd.book_genres,
                        'authors_id':book_upd.authors_id,
                        'id': book_upd.id}
