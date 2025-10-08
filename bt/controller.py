from bt.utils import io
from bt.models import Config
from bt.utils import formatter
from bt.utils import render_book
from bt.utils import render
from bt.utils.process_book import build_book
from bt.utils.logging import logger


def build_section_md(section: dict, cfg: Config) -> str:
    cover_imgs: list[str] = []

    # extracting non-book fields
    heading = render.heading(section)
    comment_before, comment_after = render.comments(section)
    section_cover_cfg: dict = section.get("cover_art", {})
    
    # bookless sections
    if section.get("books") is None:
        return "".join([
            heading,
            comment_before,
            comment_after,
        ])

    books = [build_book(b, cfg) for b in section["books"]]
    table_rows = [render_book.render_table_row(b) for b in books]
    rows_str = "\n".join(table_rows) + "\n"

    for b in books:
        if b.cover_art:
            merged_cfg = render.cover_art_cfg(cfg, section_cover_cfg)
            cover_imgs.append(render_book.render_cover_img(b, merged_cfg))


    fields = render_book.detect_fields(books)

    # set to empty
    if fields == ["Title"]:
        legend = columns = rows_str = None
    # generate columns
    else:
        legend = formatter.format_legend(fields)
        columns = formatter.format_columns(len(fields))

    art = formatter.format_art(cover_imgs)

    parts = [
        section for section in [
            heading,
            comment_before,
            legend,
            columns,
            rows_str,
            art,
            comment_after,
        ] if section
    ]
    doc = "".join(parts)

    return doc


def generate_md() -> str:
    """Generate markdown tables and headings from YAML config.

    Pulls configuration, builds book data and renders full markdown document.
    """
    cfg: Config = io.load_config()
    raw_book_progress = io.load_book_yaml()
    doc = ""

    for section in raw_book_progress["book_data"]:
        doc += build_section_md(section, cfg)
    return doc
