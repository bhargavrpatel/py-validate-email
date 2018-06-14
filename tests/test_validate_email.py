#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of py-validate-email.
# https://github.com/bhargavrpatel/py-validate-email

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2018, Bhargav Patel <ziikutv@gmail.com>

import random
from preggy import expect
from unittest import TestCase as PythonTestCase

from py_validate_email import __version__
from py_validate_email import is_email_valid
from py_validate_email import validator


class TestCase(PythonTestCase):
    pass


class VersionTestCase(TestCase):

    def test_has_proper_version(self):
        expect(__version__).to_equal("0.1.0")


class TestEmailValidator(TestCase):

    def test_invalid_email_address(self):
        """It should mark all non-emails as invalid"""
        samples = ["", " ", "\t", "      ", "some_random_string", "foo@"]
        results = map(is_email_valid, samples)
        expect(all(results)).to_equal(False)

    def test_invalid_domains(self):
        """It should mark all dispossable domain emails as invalid"""
        email = "foobar@{}".format(
            random.choice(validator._DISPOSABLE_DOMAINS)
        )
        expect(is_email_valid(email)).to_equal(False)

    def test_valid_domains(self):
        """It should allow valid domains"""
        email = "hello@gmail.com"
        expect(is_email_valid(email)).to_equal(True)
