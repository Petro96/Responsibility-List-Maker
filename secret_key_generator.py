
import random
import string


def random_generate_secret_key(length:int):

    characters = string.ascii_letters + string.digits
    secret_key = "".join(random.choice(characters) for i in range(length))
    return secret_key

print("My secret key: "+random_generate_secret_key(12))