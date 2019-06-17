import string
import random

def shortcodeGenerator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def createShortCode(instance, size=6):
    newCode = shortcodeGenerator(size=size)
    ChortUrl = instance.__class__
    qsExists = ChortUrl.objects.filter(urlShortCode=newCode).exists()
    if qsExists:
        return createShortCode(instance, size=size)
    return newCode

