#!/usr/bin/python
# -*- coding: utf-8  -*-
"""Unit tests for helpers.py."""
from __future__ import unicode_literals
import unittest
from batchupload.helpers import (
    flip_name,
    flip_names,
    get_all_template_entries,
)


class TestFlipName(unittest.TestCase):

    """Test the flip_name method."""

    def test_flip_name_empty(self):
        self.assertEquals(flip_name(''), '')

    def test_flip_name_one_part(self):
        input_value = 'The Name'
        expected = 'The Name'
        self.assertEquals(flip_name(input_value), expected)

    def test_flip_name_two_parts(self):
        input_value = 'Last, First'
        expected = 'First Last'
        self.assertEquals(flip_name(input_value), expected)

    def test_flip_name_three_parts(self):
        input_value = 'Last, Middle, First'
        expected = 'Last, Middle, First'
        self.assertEquals(flip_name(input_value), expected)


class TestFlipNames(unittest.TestCase):

    """Test the flip_names method."""

    def test_flip_names_empty(self):
        self.assertEquals(flip_names([]), [])

    # @TODO: add test counting calls to flip_names and number/content of output


class TestGetAllTemplateEntries(unittest.TestCase):

    """Test the get_all_template_entries method."""

    def test_get_all_template_entries_empty(self):
        self.assertEquals(get_all_template_entries('', ''), [])

    def test_get_all_template_entries_single(self):
        template = 'a'
        wikitext = '{{a|A|b=b|c={{c|c=pling}}}}'
        expected = [{'1': 'A', 'c': '{{c|c=pling}}', 'b': 'b'}]
        self.assertListEqual(get_all_template_entries(wikitext, template),
                             expected)

    def test_get_all_template_entries_multiple(self):
        template = 'a'
        wikitext = '{{a|b=b}} {{a|b=b}} {{a|c}}'
        expected = [{'b': 'b'}, {'b': 'b'}, {'1': 'c'}]
        self.assertListEqual(get_all_template_entries(wikitext, template),
                             expected)
