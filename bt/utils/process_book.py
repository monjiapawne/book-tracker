from bt.models import Book, Config
from bt.utils.logging import logger


def build_book(b: dict, cfg: Config) -> Book:
    """Returns a Book object from a yaml imported dict"""
    title = b.get("title")
    author = b.get("author")
    total_pages = b.get("total_pages")
    page = b.get("page")
    cover_art = b.get("cover_art")

    book = Book(title=title, author=author, total_pages=total_pages)

    logger.info(f"processing book: {title}")

    # modifications
    if page is not None:
        book.set_page(page)

    if book.page and book.total_pages:
        book.calc_progress()
        book.render_progress_bar(cfg.progress_bar)

    if b.get("cover_art"):
        book.set_cover_art(cover_art)

    return book
