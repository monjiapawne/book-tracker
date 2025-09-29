def format_columns(count: int) -> str:
    s = ""
    for i in range(count):
        s += "|--"
    s += "|"
    return f"{s}\n"


def format_legend(titles):
    legend = "| "
    for title in titles:
        legend += f"{title} |"
    return f"{legend}\n"
