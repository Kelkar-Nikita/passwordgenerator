# function to generate random passsword.
# parameter: length of password
# return: password string
import random


def passwordGenerator(length=5):
    password = random.random()
    password = str(int(password*(10**length)))
    return password

print(passwordGenerator(60))
