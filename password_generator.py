#correct user,preferences
# -length
# -should contain uppercase
# -should contain special characters
# -should contain digits

# get all available characters
# randomly,pick characters up to the length
# ensure we have at least one of each character type
# ensure length is valid


import random
import string
from xml.etree.ElementInclude import include


def password_generator():
    length = int(input("Enter the desired password length: ").strip())
    include_uppercase = input("Include upper case? (yes/no): ").lower().strip()
    include_special_characters = input("Include special characters? (yes/no): ").lower().strip()
    include_digits = input("Include digits? (yes/no): ").lower().strip()
    if length < 4:
        print("Pasword length must be at least 4 characters. ")
        return

    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation if include_special_characters == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""
    all_characters = lower + uppercase + special + digits

    required_characters = []
    if include_uppercase == "yes":
        required_characters.append(random.choice(uppercase))
    if include_special_characters == "yes":
        required_characters.append(random.choice(special))
    if include_digits == "yes":
        required_characters.append(random.choice(digits))


    remaining_length = length - len(required_characters)
    password = required_characters

    for _ in range(remaining_length):
        character = random.choice(all_characters)
        password.append(character)

    random.shuffle(password)
    str_password = "".join(password)
    return str_password

password = password_generator()
print(password)