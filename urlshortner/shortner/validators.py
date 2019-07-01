from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

## Validators

def validate_inputUrl(value):
    urlValidator = URLValidator()

    value1invalid = False
    value2invalid = False

    try:
        urlValidator(value)
    except:
        value1invalid = True

    value2url = "http://" + value

    try:
        urlValidator(value2url)
    except:
        value2invalid = True
    
    if value1invalid == False and  value2invalid == False:
        raise ValidationError("Invalid URL for this field.")

    return value

def validate_anup(value):
    if "anup" in value:
        raise ValidationError("Cannot short URLs containing my name.")
    return value