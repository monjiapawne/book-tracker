from app.models import Book
from app.utils.logging import logger

def format_book_table(book: Book, readme: str = ""):

    parts = [
        f"{book.title} |",
        f"{book.author} |" if book.author else "",
        f"{book.progress_bar} {int(book.progress)}% |" if book.progress else "",
        f"{book.page_progress} |" if book.author else ""
    ]
    
    readme += "|" + "".join(parts)
    logger.info(readme)
    return readme

def format_cover_art(book: Book, art: str = ""):
    art += f"<img src='{book.cover_art}' alt='{book.title}_cover' width='160'>"
    return art