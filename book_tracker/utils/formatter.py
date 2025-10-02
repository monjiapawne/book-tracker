def format_columns(count: int) -> str:
    if count > 0:
        s = ""
        for i in range(count):
            s += "|--"
        s += "|"
        return f"{s}\n"
    else:
        return ""


def format_legend(titles):
    legend = "| "
    for title in titles:
        legend += f"{title} |"
    return f"{legend}\n"


def format_art(images: list[str]) -> str:
    if not images:
        return ""
    return "<p align='left'>" + "".join(images) + "</p>\n\n"
