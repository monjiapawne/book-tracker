from app.controller import generate_md
from app.utils.io import write_readme
from app.utils.logging import logger


def main() -> int:
    write_readme(generate_md())
    logger.info("✅ Updated README.md")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
