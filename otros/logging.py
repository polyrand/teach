import logging
import os

FORMAT = "%(asctime)s -- %(levelname)s -- %(message)s"  # -at: "%(pathname)s:%(lineno)d"

logging.basicConfig(format=FORMAT)


# main logger
if os.getenv("LOG_LEVEL", "info") == "debug":
    log_level = logging.DEBUG
else:
    log_level = logging.INFO

log = logging.getLogger("app")
log.setLevel(log_level)
