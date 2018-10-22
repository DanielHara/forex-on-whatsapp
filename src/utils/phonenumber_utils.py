import phonenumbers


def is_valid_br_phone_number(phone_number: str) -> bool:
    try:
        parsed_number = phonenumbers.parse(phone_number, 'BR')
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.phonenumberutil.NumberParseException:
        return False

def get_e164_phone_number_from_br_number(phone_number: str) -> bool:
    if not is_valid_br_phone_number(phone_number):
        return None

    try:
        parsed_number = phonenumbers.parse(phone_number, 'BR')
        e164_phone_number = phonenumbers.format_number(
            parsed_number, phonenumbers.PhoneNumberFormat.E164)
        return e164_phone_number
    except phonenumbers.phonenumberutil.NumberParseException:
        return None
