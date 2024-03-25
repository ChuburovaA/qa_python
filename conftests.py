import pytest

@pytest.fixture
def book_dict():
    return {"name": "Гордость и предубеждение и зомби" , "genre": "Мультфильмы"}

@pytest.fixture
def book2_dict():
    return {"name": "Что делать, если ваш кот хочет вас убить", "genre": "Ужасы"}

@pytest.fixture
def children_book():
    return {"name": "Злодейка", "genre": "Ужасы"}

@pytest.fixture
def favorite_book():
    return {"name": "Гарри Поттер", "genre": "Фантастика"}