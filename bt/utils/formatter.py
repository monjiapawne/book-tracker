def format_columns(count: int) -> str:
    if count is None:
        return ""
    
    s = "|--" * count + "|"
    return f"{s}\n"


def format_legend(titles):
    legend = "| "
    for title in titles:
        legend += f"{title} |"
    return f"{legend}\n"


def format_art(images: list[str]) -> str:
    if not images:
        return ""
    return "<p align='left'>" + "".join(images) + "</p>\n\n"
