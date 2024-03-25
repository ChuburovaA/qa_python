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
