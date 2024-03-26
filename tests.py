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

    # Получение словаря books_genre
    def test_get_books_genre_add_dictionary(self, collector):
        assert collector.get_books_genre() == {}

    # Получаем список книг для детей (тут можно было использовать параметаризацию, но мне так понятнее и проще)
    def test_get_books_for_children(self, collector):
        collector.add_new_book("Book1")
        collector.set_book_genre("Book1", "Фантастика")
        collector.add_new_book("Book2")
        collector.set_book_genre("Book2", "Мультфильмы")
        collector.add_new_book("Book3")
        collector.set_book_genre("Book3", "Комедии")

        books_for_children = collector.get_books_for_children()

        assert "Book1" in books_for_children
        assert "Book2" in books_for_children
        assert "Book3" in books_for_children

# Получаем список книг недопустимые для детей (тут можно было использовать параметаризацию, но мне так понятнее и проще)
    def test_get_books_for_children_rating_not_for_children(self, collector):
        collector.add_new_book("Book1")
        collector.set_book_genre("Book1", "Фантастика")
        collector.add_new_book("Book2")
        collector.set_book_genre("Book2", "Детективы")
        collector.add_new_book("Book3")
        collector.set_book_genre("Book3", "Ужасы")

        books_for_children = collector.get_books_for_children()

        assert "Book1" in books_for_children
        assert "Book2" not in books_for_children
        assert "Book3" not in books_for_children

    # Добавление книги в избранное
    def test_add_book_in_favorites(self, collector):
        collector.add_new_book("Book1")
        collector.add_book_in_favorites("Book1")
        assert collector.get_list_of_favorites_books() == ["Book1"]

    # Добавляем книгу в избранное, которой нет в словаре
    def test_add_book_in_favorites_dont_add_in_dictionary(self, collector):
        collector.add_new_book("Book1")
        assert "Book 1" not in collector.favorites

    # Добавляем уже существующую книгу в избранное
    def test_add_existing_book_in_favorites_if_book_in_favorites(self, collector):
        collector.add_new_book("Book1")

        collector.add_book_in_favorites("Book1")
        collector.add_book_in_favorites("Book1")
        assert len(collector.get_list_of_favorites_books()) == 1

    # Удаляем книгу из избранного
    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Book1")
        collector.add_book_in_favorites("Book1")
        collector.delete_book_from_favorites("Book1")
        assert len(collector.get_list_of_favorites_books()) == 0

    # Получаем список избранных книг(тут можно было использовать параметаризацию, но мне так понятнее и проще)
    def test_get_list_of_favorites_books_add_two_books(self, collector):
        collector.add_new_book("Book1")
        collector.add_new_book("Book2")

        collector.add_book_in_favorites("Book1")
        collector.add_book_in_favorites("Book2")

        assert collector.get_list_of_favorites_books() == ["Book1", "Book2"]