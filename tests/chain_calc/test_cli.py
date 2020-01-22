#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for package `chain_calc`."""
#import pytest
from click.testing import CliRunner

from chain_calc import cli


class _TestCLI:
    """Base class to test the command line interface."""

    def call(self, args=None):
        runner = CliRunner()
        return runner.invoke(cli.main, args)

class TestBasic(_TestCLI):
    """Test basic options."""

    def test_default(self):
        result = self.call()
        assert result.exit_code == 1
        assert result.output.startswith("Usage: ")
        assert "Show this message and exit." in result.output

    def test_help(self):
        result = self.call(["--help"])
        assert result.exit_code == 0
        assert result.output.startswith("Usage: ")
        assert "Show this message and exit." in result.output

    def test_version(self):
        result = self.call(["-V"])
        assert result.exit_code == 0
        assert cli.__version__ in result.output

    def test_dry_run(self):
        result = self.call(["-n"])
        assert result.exit_code == 0
        assert "This is merely a dry run" in result.output

class TestCalcInt(_TestCLI):
    """Test calculations with integers."""

    def test_only_arg(self):
        result = self.call(["4"])
        assert result.exit_code == 0
        assert result.output.strip() == "4"

    def test_two_args(self):
        result = self.call(["4", "5"])
        assert result.exit_code == 1
        assert result.output.startswith("Error: expecting 1 number, got 2")
