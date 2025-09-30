from app.controller import main_logic
from app.utils.io import write_readme


def main():
    output = main_logic()
    write_readme(output)


if __name__ == "__main__":
    main()
