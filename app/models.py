from dataclasses import dataclass
from typing import Optional
from pathlib import Path


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
    title: str = ""
    page: Optional[int] = None
    total_pages: Optional[int] = None
    progress: int = 0
    progress_bar: str = ""
    page_progress: str = ""
    author: str = ""
    cover_art: Optional[str] = ""


    def set_page(self, value: int):
        if self.total_pages is not None and value > self.total_pages:
            self.page = self.total_pages
        else:
            self.page = value

        self.page_progress = f"{self.page}/{self.total_pages}"

    def calc_progress(self):
        self.progress = round(self.page / self.total_pages * 100, 6)

    def render_progress_bar(self, cfg: ProgressBarConfig):
        fill = cfg.fill_char
        empty = cfg.empty_char

        progress = self.progress / 100
        fill_amount = int(progress * cfg.length)

        empty_amount = cfg.length - fill_amount
        self.progress_bar = f"{fill * fill_amount}{empty * empty_amount}"

    def set_cover_art(self, cover_art: str):
        self.cover_art = Path("cover_art") / cover_art