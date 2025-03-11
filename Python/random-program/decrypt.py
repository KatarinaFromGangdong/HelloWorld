from colorlog import ColoredFormatter
from cryptography.fernet import Fernet
import logging
import time

log_level = logging.DEBUG
log_format = "  %(asctime)s [%(log_color)s%(levelname)s%(reset)s] ... %(log_color)s%(message)s%(reset)s"
logging.root.setLevel(log_level)
formatter = ColoredFormatter(log_format, datefmt="%Y-%m-%d %H:%M:%S")
stream = logging.StreamHandler()
stream.setLevel(log_level)
stream.setFormatter(formatter)
log = logging.getLogger('pythonConfig')
log.setLevel(log_level)
log.addHandler(stream)

key = input("Encryption key: ")
try:
    fernet = Fernet(key)
    time.sleep(1)
    log.info("Access Granted.")

    # THIS IS STORED IN MY DATABASE FOR EXAMPLE
    password = input("Insert encrypted message: ")
    decMessage = fernet.decrypt(password).decode()

    print("\ndecrypted string: ", decMessage)
except ValueError as e:
    time.sleep(1)
    log.error(e)
    time.sleep(1)
    log.info("System will shutdown in 5 seconds.")
    t = 5
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"  Countdown: {timer}", end="\r")
        time.sleep(1)
        t -= 1
    log.info("Bye :P")