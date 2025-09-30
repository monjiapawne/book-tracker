from app.utils.io import parse_book_yaml, process_book
from app.models import Book
from app.utils.formatter import format_legend, format_columns, format_art
from app.services.process_book_data import format_book_table, format_cover_art, detect_fields
from app.utils.logging import logger


def main_logic() -> str:
    raw_book_progress = parse_book_yaml()
    doc = ""

    # process for each heading
    for section in raw_book_progress["book_data"]:
        rows: list = []
        art_list: list[str] = []
        book_list: list[Book] = []

        heading = section["heading"]

        for b in section["books"]:
            book: Book = process_book(b)
            book_list.append(book)
            rows.append(format_book_table(book))
            
            if book.cover_art:
                art_list.append(format_cover_art(book))

        rows_all = "\n".join(rows)

        # wip
        legend_titles = detect_fields(book_list)
        if legend_titles != ["Title"]:
            legend = format_legend(legend_titles)
            columns = format_columns(len(legend_titles))
        else:
            legend = columns = rows_all = ""
            
        art = format_art(art_list)
        
        section_parts = [
            f"## {heading}\n",
            legend,
            columns,
            f"{rows_all}\n",
            art
        ]
        doc += "".join(section_parts)

    return doc
