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

    # Получаем жанр книги по её имени
    def test_get_book_genre_for_name(self, collector):
        collector.add_new_book("Book1")
        collector.set_book_genre("Book1", "Ужасы")
        assert collector.get_book_genre("Book1") == "Ужасы"

    # Получаем список книг с определённым жанром
    @pytest.mark.parametrize(
        "genre, expected_books",
        [
            ("Фантастика", ["Book1"]),
            ("Детективы", ["Book2"]),
        ]
    )
    def test_get_books_with_specific_genre(self, genre, expected_books):
        collector = BooksCollector()
        # Вывод списка книг с определённым жанром
        collector.add_new_book("Book1")
        collector.add_new_book("Book2")

        collector.set_book_genre("Book1", "Фантастика")
        collector.set_book_genre("Book2", "Детективы")

        assert collector.get_books_with_specific_genre(genre) == expected_books