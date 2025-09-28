from dataclasses import dataclass
from typing import Optional

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
