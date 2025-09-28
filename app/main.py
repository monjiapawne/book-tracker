from app.controller import main_logic
from app.io import write_readme

def main(export):
    o = main_logic()
    write_readme(o)
    return o


if __name__ == "__main__":
    result = main(1)