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
