from bt.controller import generate_md
from bt.utils.io import write_readme
from bt.utils.logging import logger


def main() -> int:
    write_readme(generate_md())
    logger.info("Updated README.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
