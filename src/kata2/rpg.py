#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    for i in range(passLen):
        password = password + random.choice(characters)

    return password
