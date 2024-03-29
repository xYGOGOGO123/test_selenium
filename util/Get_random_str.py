import random
import string


def Get_Random_Str():
    rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return rand_str

