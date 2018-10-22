from src.utils.phonenumber_utils \
    import is_valid_br_phone_number, get_e164_phone_number_from_br_number


def test_is_valid_br_phone_number():
    valid_phone_numbers = [
        '55 11 964498206',
        '+55 11 964498206',
        '+5511964498206',
        '+55 11 96449-8206',
        '+55-11-96449-8206'
    ]

    for valid_phone_number in valid_phone_numbers:
        assert is_valid_br_phone_number(valid_phone_number)

    unvalid_phone_numbers = [
        '+55 1 964498206',
        'whatever',
        '+55 11250 1526301895540'
    ]

    for unvalid_phone_number in unvalid_phone_numbers:
        assert not is_valid_br_phone_number(unvalid_phone_number)

def test_get_e164_phone_number_from_br_number():
    e164_phone_number = '+5511964498206'

    assert get_e164_phone_number_from_br_number('55 11 964498206') == e164_phone_number
    assert get_e164_phone_number_from_br_number('+55 11 964498206') == e164_phone_number
    assert get_e164_phone_number_from_br_number('+5511964498206') == e164_phone_number
    assert get_e164_phone_number_from_br_number('+55 11 96449-8206') == e164_phone_number
    assert get_e164_phone_number_from_br_number('+55-11-96449-8206') == e164_phone_number

    assert  get_e164_phone_number_from_br_number('+55 1 964498206') is None
    assert  get_e164_phone_number_from_br_number('whatever') is None
    assert  get_e164_phone_number_from_br_number('+55 11250 1526301895540') is None
