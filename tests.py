from main import BooksCollector

class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # Установить жанр книги которой нет в словаре
    def test_set_book_genre(self, book2_dict):
        collector = BooksCollector()
        collector.set_book_genre(book2_dict["name"], book2_dict["genre"])
        assert collector.get_book_genre(book2_dict["name"]) is None

# Устанавливаем жанр книги, которая есть в словаре и жанр допустимый
    def test_set_book_genre_have_in_dictionary(self, book_dict):
        collector = BooksCollector()
        collector.add_new_book(book_dict["name"])
        collector.set_book_genre(book_dict["name"], book_dict["genre"])
        assert collector.get_book_genre(book_dict["name"]) == "Мультфильмы"

    # Получаем список книг с жанром, которого нет в списке доступных жанров
    def test_get_books_with_specific_genre_add_new_genre(self, book_dict, book2_dict):
        collector = BooksCollector()

        collector.add_new_book(book_dict["name"])
        collector.add_new_book(book2_dict["name"])

        collector.set_book_genre(book_dict["name"], "Роман")
        collector.set_book_genre(book2_dict["name"], "Роман")

        assert collector.get_books_with_specific_genre("Роман") == []