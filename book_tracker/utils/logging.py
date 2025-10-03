import logging

LOG_FORMAT = "[%(levelname)s] [%(funcName)s] %(message)s"

logging.basicConfig(
    level=logging.DEBUG,
    format=LOG_FORMAT,
)

logger = logging.getLogger("app")

# supressing PIL logs
logging.getLogger("PIL").setLevel(logging.WARNING)
logging.getLogger("PIL.ImageFile").setLevel(logging.WARNING)
logging.getLogger("PIL.PngImagePlugin").setLevel(logging.WARNING)
