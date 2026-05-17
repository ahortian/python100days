from day1_validate_email import validate_email


def test_validate_email_accepts_valid_address():
    assert validate_email("user@example.com") is True


def test_validate_email_rejects_invalid_address():
    assert validate_email("invalid-email@@example") is False
