from app.models import Book

def format_book_table(book: Book, readme: str = ""):
    parts = [
        f"{book.title} |",
        f"{book.author} |" if book.author else " |",
        f"{book.progress_bar} {int(book.progress)}% |" if book.progress else " |",
        f"{book.page_progress} |" if book.page_progress else " |"
    ]
    
    readme += "|" + "".join(parts)
    return readme


def format_cover_art(book: Book, art: str = ""):
    art += f"<img src='{book.cover_art}' alt='{book.title}_cover' width='160'>"
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

