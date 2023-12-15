from typing import List
from fastapi import APIRouter, HTTPException

from . import db_manager
from .models import BookIn, BookOut, BookUpdate

books = APIRouter()


@books.get("/", response_model=List[BookOut], status_code=200)
async def list_book() -> dict:
    """
    Получить все книги
    """
    return await db_manager.get_all_books()


@books.get("/{book_id}", response_model=BookOut, status_code=200)
async def get_book(book_id: int):
    """
    Получить одну книгу по ID
    """
    book = await db_manager.get_book(book_id)
    if not book:
        HTTPException(status_code=404, detail="Book not found")
    return book


@books.post("/create/", response_model=BookOut, status_code=201)
async def create_book(payload: BookIn):
    """
    Создать книгу
    """

    book_id = await db_manager.add_book(payload)
    response = {"id": book_id, **payload.dict()}
    return response


@books.put("/update/{book_id}/", response_model=BookOut)
async def update_book(book_id: int, payload: BookUpdate):
    """
    Обновить книгу
    """
    book = await db_manager.get_book(book_id)

    if not book:
        HTTPException(status_code=404, detail="Book not found")

    update_data = payload.dict(exclude_unset=True)

    book_id_db = BookIn(**book)
    update_book = book_id_db.copy(update=update_data)
    return await db_manager.update_book(book_id, update_book)


@books.delete("/delete/{book_id}/", response_model=None)
async def delete_book(book_id: int):
    """
    Удалить книгу
    """
    book = await db_manager.get_book(book_id)
    if not book:
        HTTPException(status_code=404, detail="Book not found")
    return await db_manager.delete_book(book_id)
