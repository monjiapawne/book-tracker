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
    # tilt
    # clean
    addons_clean = (
        "border-radius:12px; "
        "box-shadow:0 4px 8px rgba(0,0,0,0.3); "
        "filter: brightness(105%) contrast(105%); "
        "padding:4px; "
    )

    # Neon glow
    addons_neon = (
        "border-radius:8px; "
        "box-shadow:0 0 12px rgba(0,255,255,0.8); "
        "filter: brightness(120%) saturate(150%); "
    )

    # Vintage / Sepia
    addons_vintage = (
        "border: 2px solid #654321; "
        "filter: sepia(100%) contrast(120%) brightness(90%); "
    )

    # Black & White
    addons_bw = (
        "filter: grayscale(100%) contrast(110%); "
    )

    # tilt
    deg = random.randint(-3, 3)
    scale = random.uniform(1, 1.1)
    # Tilted / Dynamic
    addons_tilt = (
        "border-radius:6px; "
        "box-shadow:0 6px 10px rgba(0,0,0,0.4); "
        f"transform: rotate({deg}deg) scale({scale}); "
    )

    # Glow / Highlight
    addons_glow = (
        "filter: drop-shadow(0 0 8px gold) brightness(115%); "
    )


    art += (
        f"<img src='{book.cover_art}' alt='{book.title}_cover' "
        f"style='width:{config.width * config.scale}px; height:{config.height * config.scale}px; "
        f"object-fit:cover; margin:{config.margin}px; "
        f"display:inline-block; vertical-align:top; "
        f"{addons_tilt}"
        f"'/>"
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
