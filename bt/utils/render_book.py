from bt.models import Book, CoverArt
from bt.utils.logging import logger
from bt.models import Book
from bt.utils.process_images import resize_image


def render_table_row(book: Book, readme: str = ""):
    parts = [
        f"{book.title} |",
        f"{book.author} |" if book.author else " |",
        f"{book.progress_bar} {int(book.progress)}% |" if book.progress else " |",
        f"{book.page_progress} |" if book.page_progress else " |",
    ]

    readme += "|" + "".join(parts)
    return readme


def render_cover_img(book: Book, config: CoverArt, art: str = "") -> str:
    width = int(config.width * (config.scale / 2))
    height = int(config.height * (config.scale / 2))
    cover_art_path = resize_image(
        book.cover_art, width=config.width, height=config.height
    )
    art += (
        f"<img src='{cover_art_path}' alt='{book.title}_cover' "
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
