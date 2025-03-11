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

data = input("Enter your message to encrypt: ")

key = Fernet.generate_key()

fernet = Fernet(key)

encMessage = fernet.encrypt(data.encode())

time.sleep(1)
log.info("Message Encrypted.")
# print(f"\nEncryption key: {key}")
# print(f"Encrypted message: {key}{encMessage}")
with open(f"{key}.txt", "w") as ef:
    ef.write(f"{encMessage}")
time.sleep(1)
log.info("File saved as .txt")
time.sleep(10)
