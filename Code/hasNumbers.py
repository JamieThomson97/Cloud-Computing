import sys
import re



def filter(inputString):
    if inputString is "www":
        return True


def lower_removePunct(inputString):
    punct_removed_lower =  re.sub(r"[^A-z ']", " ", inputString.lower())
    return  punct_removed_lower

print (lower_removePunct("Ja!£,m'ie"))