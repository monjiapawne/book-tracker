from app.io import parse_book_yaml, process_book
from app.models import Book
from app.formatter import format_legend, format_columns


def main_logic():
    raw_book_progress = parse_book_yaml()
    o = ""
    x = ""
    legend_titles = ["Title"]
    for section in raw_book_progress["book_data"]:

        heading = section["heading"]

        for b in section["books"]:
            book = process_book(b)

            o += "|"
            o += f" {book.title} |"

            if book.author:
                o += f"{book.author} |"
                if "Author" not in legend_titles:
                    legend_titles.append("Author")

            if book.progress_bar:
                o += f"{book.progress_bar} {int(book.progress)}% |"
                if "Progress" not in legend_titles:
                    legend_titles.append("Progress")

            if book.page_progress:
                o += f"{book.page_progress} |"
                if "Page" not in legend_titles:
                    legend_titles.append("Page")

            if book.cover_art:
                o += f"\n[{book.title}_cover]({book.cover_art})"

            o += "\n"

            legend = format_legend(legend_titles)

        columns = format_columns(len(legend_titles))
        x += f"## {heading}\n{legend}{columns}{o}\n"
        o = ""
        legend_titles = ["Title"]

    return x
