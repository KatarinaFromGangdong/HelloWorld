import random
import string

# Define the length of the password
password_length = 64

# Define the character set to use for the password
character_set = string.ascii_letters + string.digits + string.punctuation

# Generate the password
password = ''.join(random.choice(character_set)
                   for i in range(password_length))

# Print the password
print("64 bit pass code --> ", password)
