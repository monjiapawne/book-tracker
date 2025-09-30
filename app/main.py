from app.controller import generate_md
from app.utils.io import write_readme


def main():
    write_readme(generate_md())


if __name__ == "__main__":
    main()
