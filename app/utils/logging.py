import logging

LOG_FORMAT = "[%(levelname)s] [%(funcName)s] %(message)s"

logging.basicConfig(
    level=logging.WARNING,
    format=LOG_FORMAT,
)

logger = logging.getLogger("app")