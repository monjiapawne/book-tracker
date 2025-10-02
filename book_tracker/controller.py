from book_tracker.utils.io import load_book_yaml, load_config
from book_tracker.models import Book, CoverArt
from book_tracker.utils.formatter import format_legend, format_columns, format_art
from book_tracker.utils.render_book import (
    render_table_row,
    render_cover_img,
    detect_fields,
)
from book_tracker.utils.process_book import build_book
from book_tracker.utils.logging import logger


def generate_md() -> str:
    """Return markdown formated tables and headings
    
    High level, pull yaml, generate books, generate markdown table
    """
    cfg = load_config()
    raw_book_progress = load_book_yaml()
    doc = ""

    for section in raw_book_progress["book_data"]:
        table_rows: list = []
        cover_imgs: list[str] = []
        books: list[Book] = []

        heading = section["heading"]
        logger.info(f"processing section: {heading}")

        section_cover_cfg: dict = section.get("cover_art", {})

        for b in section["books"]:
            book: Book = build_book(b, cfg)
            books.append(book)
            table_rows.append(render_table_row(book))

            if book.cover_art:
                # unpack global config and local. local overlap global
                merged_dict = {**cfg.cover_art.__dict__, **section_cover_cfg}
                # create a new object to pass in
                merged_cfg = CoverArt(**merged_dict)
                cover_imgs.append(render_cover_img(book, merged_cfg))

        rows_str = "\n".join(table_rows)

        fields = detect_fields(books)
        if fields != ["Title"]:
            legend = format_legend(fields)
            columns = format_columns(len(fields))
        else:
            legend = columns = rows_str = ""

        art = format_art(cover_imgs)

        parts = [f"## {heading}\n", legend, columns, f"{rows_str}\n", art]
        doc += "".join(parts)

    return doc
