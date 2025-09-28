from app.models import ProgressBarConfig


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
