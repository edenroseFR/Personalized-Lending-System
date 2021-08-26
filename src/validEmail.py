import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def validEmail(email=None):
    if(re.fullmatch(regex, email)):
        return True

