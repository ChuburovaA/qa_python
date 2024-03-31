# qa_python
Проверка тестов:
tests.py::TestBooksCollector::test_add_new_book_add_two_books PASSED     [  7%]
tests.py::TestBooksCollector::test_set_book_genre_add_genre_new_book PASSED [ 14%]
tests.py::TestBooksCollector::test_set_book_genre_to_non_existing_book PASSED [ 21%]
tests.py::TestBooksCollector::test_get_book_genre_for_name PASSED        [ 28%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre[\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430-expected_books0] PASSED [ 35%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre[\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432\u044b-expected_books1] PASSED [ 42%]
tests.py::TestBooksCollector::test_get_books_genre_add_dictionary PASSED [ 50%]
tests.py::TestBooksCollector::test_get_books_for_children PASSED         [ 57%]
tests.py::TestBooksCollector::test_get_books_for_children_rating_not_for_children PASSED [ 64%]
tests.py::TestBooksCollector::test_add_book_in_favorites PASSED          [ 71%]
tests.py::TestBooksCollector::test_add_book_in_favorites_dont_add_in_dictionary PASSED [ 78%]
tests.py::TestBooksCollector::test_add_existing_book_in_favorites_if_book_in_favorites PASSED [ 85%]
tests.py::TestBooksCollector::test_delete_book_from_favorites PASSED     [ 92%]
tests.py::TestBooksCollector::test_get_list_of_favorites_books_add_two_books PASSED [100%]

============================= 14 passed in 0.05s ==============================
Было проведено тестирование (юнит тестирование) содержащие в себе фиксуру (для удобства тестирования) и был применен так же метод параметаризации.
Я покрывала тестами приложение, которое устанваливает жанр к книге и способно добавлять книги в избранное.
Так же была проведена проверка на возрастной жанар - то что можно читать детям, а что нельзя.

Был проверен каждый блок. Все тесты прошли проверку.


