from app.controller import main_logic
from app.io import write_readme

def main(export):
    output = main_logic()
    write_readme(output)


if __name__ == "__main__":
    main()