from app.utils.io import parse_book_yaml, process_book
from app.models import Book
from app.utils.formatter import format_legend, format_columns
from app.services.process_book_data import format_book_table, format_cover_art


def main_logic():
    raw_book_progress = parse_book_yaml()
    readme = ""
    x = ""
    art = ""
    art_start = ""
    art_end = ""

    legend_titles = ["Title", "Author", "Progress", "Page"]
    for section in raw_book_progress["book_data"]:

        heading = section["heading"]

        for b in section["books"]:
            book = process_book(b)

            readme += format_book_table(book)
            if book.cover_art:
                art += format_cover_art(book)


                if len(legend_titles) == 1:
                    legend_titles = []
                    art_start = "<p align='left'>"
                    art_end = "</p>\n\n"
                    
                readme = ""
            readme += "\n"

            legend = format_legend(legend_titles)

        columns = format_columns(len(legend_titles))
        # duct tape
        x += f"## {heading}\n{legend}{columns}{readme}\n{art_start}{art_start}{art}{art_end}"
        art = ""
        readme = ""
        legend_titles = ["Title"]

    return x
