from app.io import parse_book_yaml, process_book
from app.models import Book


HEADER = """\
| Title        | Author | Progress                   | Page                 |
|--------------|--------|----------------------------|----------------------|\n"""


def main_logic():
    raw_book_progress = parse_book_yaml()

    o = ""
    for section in raw_book_progress["book_data"]:
        heading = section["heading"]
        o += f"## {heading}\n"
        o += HEADER

        for b in section["books"]:
            book = process_book(b)
            o += f"| {book.title} | {book.author} | {book.progress_bar} {book.progress}% | {book.page_progress} |\n"

    return o
