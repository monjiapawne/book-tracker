from app.models import Book, CoverArt
from app.utils.logging import logger
from app.models import Book, Config
import random

def format_book_table(book: Book, readme: str = ""):
    parts = [
        f"{book.title} |",
        f"{book.author} |" if book.author else " |",
        f"{book.progress_bar} {int(book.progress)}% |" if book.progress else " |",
        f"{book.page_progress} |" if book.page_progress else " |"
    ]
    
    readme += "|" + "".join(parts)
    return readme


def format_cover_art(book: Book, config: CoverArt, art: str = "") -> str:
    width = int(config.width * config.scale)
    height = int(config.height * config.scale)

    art += (
        f"<img src='{book.cover_art}' alt='{book.title}_cover' "
        f"width='{width}' height='{height}'>"
    )
    return art


def detect_fields(books: list[Book]) -> list[str]:
    fields = ["Title"]
    if any(b.author for b in books):
        fields.append("Author")
    if any(b.progress for b in books):
        fields.append("Progress")
    if any(b.page_progress for b in books):
        fields.append("Page")
        
    return fields


# ---------- core book ingestion -------- #
def process_book(b, cfg: Config) -> Book:
    book = Book()

    book.title = b.get("title")
    logger.info(f"processing book: {book.title}")
    book.author = b.get("author", None)

    book.total_pages = b.get("total_pages", None)

    if b.get("page"):
        book.set_page(b["page"])

    if book.page and book.total_pages:
        book.calc_progress()
        book.render_progress_bar(cfg.progress_bar)

    if b.get("cover_art"):
        book.set_cover_art(b["cover_art"])

    return book
