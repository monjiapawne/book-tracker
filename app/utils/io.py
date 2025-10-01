import yaml
from pathlib import Path
from app.models import Config, ProgressBarConfig, Book, CoverArt
from app.utils.logging import logger

ROOT_DIR = Path(__file__).resolve().parent.parent.parent


def parse_config() -> Config:
    with open(ROOT_DIR / "config.yaml", "r") as f:
        raw = yaml.safe_load(f)

    return Config(
        progress_bar=ProgressBarConfig(**raw["config"]["progress_bar"]),
        cover_art=CoverArt(**raw["config"]["global_cover_art"])
    )


# ---------- helpers -------- #
def parse_book_yaml():
    with open(ROOT_DIR / "book_progress.yaml", "r") as f:
        data = yaml.safe_load(f.read())
    return data


def write_readme(s: str) -> None:
    with open(ROOT_DIR / "README.md", "w") as f:
        f.write(s)


