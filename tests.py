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

    # Получаем список книг с существующим жанром
    def test_get_books_with_specific_genre_have_in_dictionary(self, book_dict, book2_dict):
        collector = BooksCollector()

        collector.set_book_genre(book_dict["name"], "Фантастика")
        collector.set_book_genre(book2_dict["name"], "Фантастика")

        assert collector.get_books_with_specific_genre("Фантастика") == [book_dict["name"], book2_dict["name"]]

    #Список книг для детей с подходящим жанром
    def test_get_books_for_children_genre_for_children(self):
        collector = BooksCollector()

        collector.add_new_book("Мышка в поле")
        collector.add_new_book("Сказка про математику")

        collector.set_book_genre("Мышка в поле", "Комедия")
        collector.set_book_genre("Сказка про математику", "Комедия")

        assert collector.get_books_for_children() == ["Мышка в поле", "Сказка про математику"]

    # Список книг для детей с неподходящим жанром
    def test_get_books_for_children_genre_for_not_children(self, children_book):
        collector = BooksCollector()

        collector.add_new_book(children_book["genre"])
        collector.set_book_genre(children_book["name"], children_book["genre"])
        assert collector.get_books_for_children() is None

    # Добавляем книгу в избранное
    def test_add_book_in_favorites_new_book(self, favorite_book):
        collector = BooksCollector()

        collector.add_new_book(favorite_book["name"])
        collector.set_book_genre(favorite_book["name"], favorite_book["genre"])
        collector.add_book_in_favorites(favorite_book["genre"])

        assert collector.favorites == [favorite_book["name"]]

    # Удаляем книгу из избранного
    def test_delete_book_from_favorites_get_book(self, favorite_book):
        collector = BooksCollector()

        collector.add_new_book(favorite_book["name"])
        collector.set_book_genre(favorite_book["name"], favorite_book["genre"])
        collector.add_book_in_favorites(favorite_book["name"])
        collector.delete_book_from_favorites(favorite_book["name"])

        assert collector.delete_book_from_favorites(favorite_book["name"]) is None