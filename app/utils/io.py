import yaml
from pathlib import Path
from app.models import Config, ProgressBarConfig, Book
from app.utils.logging import logger

ROOT_DIR = Path(__file__).resolve().parent.parent.parent


def parse_config() -> Config:
    with open(ROOT_DIR / "config.yaml", "r") as f:
        raw = yaml.safe_load(f.read())

    return Config(progress_bar=ProgressBarConfig(**raw["config"]["progress_bar"]))


# ---------- helpers -------- #
def parse_book_yaml():
    with open(ROOT_DIR / "book_progress.yaml", "r") as f:
        data = yaml.safe_load(f.read())
    return data


def write_readme(s: str) -> None:
    with open(ROOT_DIR / "README.md", "w") as f:
        f.write(s)


# ---------- core book ingestion -------- #
def process_book(b) -> Book:
    cfg = parse_config()
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