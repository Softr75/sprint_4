from main import BooksCollector
import pytest

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
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
    def test_set_and_get_book_genre(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == genre

    @pytest.mark.parametrize(
            "genre, expected_books",
            [
                ("Фантастика", ["Гарри Поттер"]),
                ("Ужасы", ["Оно"]),
                ("Детективы", ["Шерлок Холмс"])
            ]
    )
    def test_get_books_with_specific_genre(self, genre, expected_books):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Шерлок Холмс", "Детективы")
        assert collector.get_books_with_specific_genre(genre) == expected_books

    def test_get_books_genre_dict(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        assert isinstance(collector.get_books_genre(), dict)

    def test_get_books_for_children(self):
        collector = BooksCollector()
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
    def test_add_and_delete_book_in_favorites(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert book in collector.get_list_of_favorites_books()
        collector.delete_book_from_favorites(book)
        assert book not in collector.get_list_of_favorites_books()