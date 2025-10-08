from bt.models import Book, CoverArt, Config

def heading(section: dict) -> str:
    heading = section["heading"]
    heading_depth = int(section.get("heading_depth", 2))
    return f"{'#' * heading_depth} {heading}\n"


def comments(section: dict) -> tuple[str, str]:
    comments_before = section.get("comment_before", "").splitlines()
    comment_before = "  \n".join(comments_before) + "\n"
    comments_after = section.get("comment_after", "").splitlines()
    comment_after = "  \n".join(comments_after) + "\n"
    return comment_before, comment_after


def cover_art_cfg(cfg: Config, section_cover_cfg: dict):
    merged_dict = {**cfg.cover_art.__dict__, **section_cover_cfg}
    return CoverArt(**merged_dict)