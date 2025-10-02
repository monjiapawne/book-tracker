from app.utils.io import parse_book_yaml, parse_config
from app.models import Book, CoverArt
from app.utils.formatter import format_legend, format_columns, format_art
from app.utils.process_book_data import format_book_table, format_cover_art, detect_fields, process_book
from app.utils.logging import logger


def generate_md() -> str:
    cfg = parse_config()
    raw_book_progress = parse_book_yaml()
    doc = ""

    for section in raw_book_progress["book_data"]:
        rows: list = []
        art_list: list[str] = []
        book_list: list[Book] = []

        heading = section["heading"]
        logger.info(f"processing section: {heading}")

        section_cover_cfg: dict = section.get("cover_art", {})

        for b in section["books"]:
            book: Book = process_book(b, cfg)
            book_list.append(book)
            rows.append(format_book_table(book))
            

            if book.cover_art:
                # unpack global config and local. local overlap global
                merged_dict = {**cfg.cover_art.__dict__, **section_cover_cfg}
                # create a new object to pass in
                merged_cfg = CoverArt(**merged_dict)
                art_list.append(format_cover_art(book, merged_cfg))

        rows_all = "\n".join(rows)

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
