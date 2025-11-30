from main import BooksCollector
import pytest

@pytest.fixture
def collector():
    return BooksCollector()

class TestBooksCollector:
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize(
        "book, genre",
        [
            ("Гарри Поттер", "Фантастика"),
            ("Оно", "Ужасы"),
            ("Шерлок Холмс", "Детективы")
        ]
    )
    def test_set_book_genre(self, book, genre, collector):
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == genre

    def test_get_book_genre_by_name(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.books_genre["Гарри Поттер"] = "Фантастика"
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

    def test_get_book_genre_nonexistent(self, collector):
        assert collector.get_book_genre("Фэнтези") is None

    @pytest.mark.parametrize(
            "genre, expected_books",
            [
                ("Фантастика", ["Гарри Поттер"]),
                ("Ужасы", ["Оно"]),
                ("Детективы", ["Шерлок Холмс"])
            ]
    )
    def test_get_books_with_specific_genre(self, genre, expected_books, collector):
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Шерлок Холмс", "Детективы") 
        assert collector.get_books_with_specific_genre(genre) == expected_books

    def test_get_books_genre_dict(self, collector):
        collector.add_new_book("Гарри Поттер")
        assert isinstance(collector.get_books_genre(), dict)

    def test_get_books_for_children(self, collector):
        books = [("Гарри Поттер", "Фантастика"),
                 ("Оно", "Ужасы"),
                 ("Шерлок Холмс", "Детективы")]
        for book, genre in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        assert sorted(collector.get_books_for_children()) == sorted(["Гарри Поттер"])

    @pytest.mark.parametrize(
            "book",
            ("Гарри Поттер", "Оно", "1984")
    )
    def test_add_book_in_favorites(self, book, collector):
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert book in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize(
            "book",
            ("Гарри Поттер", "Оно", "1984")
    )
    def test_delete_book_in_favorites(self, book, collector):
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)
        assert book not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize(
            "book",
            ("Гарри Поттер", "Оно", "1984")
    )
    def test_get_list_of_favorite_books(self, book, collector):
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert book in collector.get_list_of_favorites_books()