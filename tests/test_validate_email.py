#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of py-validate-email.
# https://github.com/bhargavrpatel/py-validate-email

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2018, Bhargav Patel <ziikutv@gmail.com>

from preggy import expect
from unittest import TestCase as PythonTestCase

from py_validate_email import __version__


class TestCase(PythonTestCase):
    pass


class VersionTestCase(TestCase):
    def test_has_proper_version(self):
        expect(__version__).to_equal('0.1.0')
