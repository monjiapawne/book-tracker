from app.models import Book, CoverArt

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
    art += (
        f"<img src='{book.cover_art}' alt='{book.title}_cover' "
        f"style='width:{config.width * config.scale}px; height:{config.height * config.scale}px; "
        f"object-fit:cover; margin:{config.margin}px; "
        f"display:inline-block; vertical-align:top;'/>"
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

