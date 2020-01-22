#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `chain_calc/utils.py` package."""
import logging

import pytest
from click.testing import CliRunner

from chain_calc import utils


# dummy lines to avoid flake8 error F401 (imported but unused); remove!
pytest
CliRunner


def test_count_to_log_level():
    assert utils.count_to_log_level(0) == logging.ERROR
    assert utils.count_to_log_level(1) == logging.WARNING
    assert utils.count_to_log_level(2) == logging.INFO
    assert utils.count_to_log_level(3) == logging.DEBUG
