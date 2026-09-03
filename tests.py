from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    
    # 1. затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
        
    # 2. add_new_book — параметризация: граничные значения длины названия
    @pytest.mark.parametrize('name, expected', [
        ('', False),                          # пустое — не добавится
        ('А', True),                           # 1 символ — добавится
        ('К' * 40, True),                      # ровно 40 — добавится
        ('К' * 41, False),                     # 41 — не добавится
    ])
    def test_add_new_book_name_length_boundaries(self, name, expected):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert (name in collector.get_books_genre()) == expected

    # 3. set_book_genre — жанр устанавливается для существующей книги
    def test_set_book_genre_for_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    # 4. get_book_genre — выводит жанр книги по её имени
    def test_get_genre_for_existing_book(self):
        collector = BooksCollector()
        book_name = "Властелин колец"
        expected_genre = "Фантастика"
        collector.books_genre[book_name] = expected_genre
        result = collector.get_book_genre(book_name)
        assert result == expected_genre

    # 5. get_books_with_specific_genre — фильтр по жанру
    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Оно')
        collector.add_new_book('Шрек')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        result = collector.get_books_with_specific_genre('Фантастика')
        assert result == ['Дюна']

    # 6. get_books_genre — возвращает текущий словарь
    def test_get_books_genre_returns_dict(self):
            collector = BooksCollector()
            collector.add_new_book('Дюна')
            result = collector.get_books_genre()
            assert result == {'Дюна': ''}
    
    # 7. get_books_for_children — возрастной рейтинг исключается
    def test_get_books_for_children_excludes_age_rated_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Маша и Медведь')
        collector.add_new_book('Оно')
        collector.add_new_book('Дюна')
        collector.set_book_genre('Маша и Медведь', 'Мультфильмы')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Дюна', 'Фантастика')
        result = collector.get_books_for_children()
        assert 'Маша и Медведь' in result
        assert 'Дюна' in result
        assert 'Оно' not in result

    # 8. add_book_in_favorites — нельзя добавить книгу, которой нет в books_genre
    def test_add_book_in_favorites_unknown_book_not_added(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert collector.get_list_of_favorites_books() == []

    # 9. delete_book_from_favorites — удаление существующей книги
    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Дюна')
        assert 'Дюна' not in collector.get_list_of_favorites_books()

    # 10. get_list_of_favorites_books — получает список избранных книг 
    def test_get_list_of_favorites_books_with_items():
        collector = BooksCollector()
        collector.favorites = ["Война и мир", "Преступление и наказание"]
        result = collector.get_list_of_favorites_books()
        assert result == ["Война и мир", "Преступление и наказание"]
        assert isinstance(result, list)
    