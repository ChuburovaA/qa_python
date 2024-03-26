import pytest
from main import BooksCollector
# Понимаю что фиксуру нужно писать в отдельном файле (conftests.py), но у меня не получается его работа оттуда
@pytest.fixture
def collector():
    return BooksCollector()


class TestBooksCollector:
    # Проверка добавления книги
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book("Book1")
        collector.add_new_book("Book2")

        assert len(collector.books_genre) == 2

    # Установка жанра книге
    def test_set_book_genre_add_genre_new_book(self, collector):
        collector.add_new_book("Book1")
        collector.set_book_genre("Book1", "Фантастика")
        assert collector.get_book_genre("Book1") == "Фантастика"

    # Устанавливаем жанр книге которой нет в словаре
    def test_set_book_genre_to_non_existing_book(self, collector):
        collector.set_book_genre("Book1", "Фантастика")
        assert collector.get_book_genre("Book1") is None