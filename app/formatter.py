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
    if len(titles) > 0:
        legend = "| "
        for title in titles:
            legend += f"{title} |"
        return f"{legend}\n"
    else:
        return ""
