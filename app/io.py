import yaml
from pathlib import Path
from app.models import Config, ProgressBarConfig, Book
from app.helpers import calc_progress, render_progress_bar

ROOT_DIR = Path(__file__).resolve().parent.parent


def parse_config() -> Config:
    with open(ROOT_DIR / 'config.yaml', 'r') as f:
        raw = yaml.safe_load(f.read())

    return Config(
        progress_bar=ProgressBarConfig(**raw["config"]["progress_bar"])
    )


def parse_book_yaml():
    with open(ROOT_DIR / 'book_progress.yaml', 'r') as f:
        data = yaml.safe_load(f.read())
    return data


def process_book(book_data) -> Book:
    cfg = parse_config()
    
    total_pages = book_data['total_pages']
    page = book_data['page']
    if page > total_pages:
        page = total_pages

    title = book_data.get('title') or ""

    progress: float = calc_progress(page, total_pages)
    progress_bar = render_progress_bar(progress, cfg.progress_bar)

    author: str = book_data.get('author', "")

    book = Book(
        title=title, 
        page_progress=f"{page}/{total_pages}",
        progress=int(progress),
        progress_bar=progress_bar,
        author=author
    )

    return book


def write_readme(s: str) -> None:
    with open(ROOT_DIR / 'README.md', 'w') as f:
        f.write(s)

