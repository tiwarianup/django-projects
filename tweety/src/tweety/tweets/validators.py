from django.core.exceptions import ValidationError

def validateTweetText(value):
    tweetText = value
    if tweetText == "anup":
        raise ValidationError("The tweet cannot have my name!")
    return value