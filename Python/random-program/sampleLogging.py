import logging
log_level = logging.DEBUG
log_format = "  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
from colorlog import ColoredFormatter
logging.root.setLevel(log_level)
formatter = ColoredFormatter(log_format)
stream = logging.StreamHandler()
stream.setLevel(log_level)
stream.setFormatter(formatter)
log = logging.getLogger('pythonConfig')
log.setLevel(log_level)
log.addHandler(stream)

log.debug("A quirky message only developers care about")
log.info("Curious users might want to know this")
log.warning("Something is wrong and any user should be informed")
log.error("Serious stuff, this is red for a reason")
log.critical("OH NO everything is on fire")