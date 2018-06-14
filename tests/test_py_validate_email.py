import random

from py_validate_email import is_valid_email
from py_validate_email import email_validator as validator


def test_invalid_email_address():
    """It should mark all non-emails as invalid"""
    samples = ["", " ", "\t", "      ", "some_random_string", "foo@"]
    results = map(is_valid_email, samples)
    assert all(results) is False


def test_invalid_domains():
    """It should mark all dispossable domain emails as invalid"""
    email = "foobar@{}".format(random.choice(validator._DISPOSABLE_DOMAINS))
    assert is_valid_email(email) is False


def test_valid_domains():
    """It should allow valid domains"""
    email = "hello@gmail.com"
    assert is_valid_email("hello@gmail.com") is True


def test_invalidating_plus_symbol():
    """It should invalidate emails with aliases if disabled"""
    assert is_valid_email("hello+hi@gmail.com", allow_plus=False) is False
