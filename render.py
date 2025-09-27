from dataclasses import dataclass
from typing import Optional
import yaml

# ----------------- config ------------------- #
@dataclass
class ProgressBarConfig:
    length: int
    fill_char: str
    empty_char: str

@dataclass
class Config:
    progress_bar: ProgressBarConfig

@dataclass
class Book:
    title: str
    page_progress: str
    progress: int
    progress_bar: str
    author: Optional[str] = None


# ----------------- helpers --------------- #
def render_progress_bar(progress: float, cfg: ProgressBarConfig):
    fill = cfg.fill_char
    empty = cfg.empty_char

    progress = progress / 100
    fill_amount = int(progress * cfg.length)
    
    empty_amount = cfg.length - fill_amount
    pb = f"{fill * fill_amount}{empty * empty_amount}"
    
    return pb


def calc_progress(page: float, total_pages: float) -> int:
    return round(page / total_pages * 100, 6)


# ----------------- config -------------------- #
def parse_config() -> Config:
    with open('config.yaml', 'r') as f:
        raw = yaml.safe_load(f.read())

    return Config(
        progress_bar=ProgressBarConfig(**raw["config"]["progress_bar"])
    )


# ----------------- book -------------------- #
def parse_yaml() -> list[Book]:
    cfg = parse_config()

    with open('book_progress.yaml', 'r') as f:
        data = yaml.safe_load(f.read())

    bookList = []
    for i, b in enumerate(data["books"], 1):
        total_pages = b['total_pages']
        page = b['page']
        if page > total_pages:
            page = total_pages

        title = b.get('title') or f"book{i}"

        progress: float = calc_progress(page, total_pages)
        progress_bar = render_progress_bar(progress, cfg.progress_bar)

        author: str = b.get('author', "")

        book = Book(
            title=title, 
            page_progress=f"{page}/{total_pages}",
            progress=int(progress),
            progress_bar=progress_bar,
            author=author
        )

        bookList.append(book)
    
    return bookList


# ----------------- main ------------------- #
def main(export):
    bookList = parse_yaml()
    
    o = """\
| Title        | Author | Progress                   | Page                 |
|--------------|--------|----------------------------|----------------------|\n"""
    if export:
        for book in bookList:
            o += f"| {book.title} | {book.author} | {book.progress_bar} {book.progress}% | {book.page_progress} |\n"
        
    with open('README.md', 'w') as f:
        f.write(o)

if __name__ == "__main__":
    main(1)