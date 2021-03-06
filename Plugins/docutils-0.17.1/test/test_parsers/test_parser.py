#! /usr/bin/env python

# $Id: test_parser.py 8367 2019-08-27 12:09:56Z milde $
# Author: Stefan Rank <strank(AT)strank(DOT)info>
# Copyright: This module has been placed in the public domain.

"""
Tests for basic functionality of parser classes.
"""

import sys
import unittest
import DocutilsTestSupport              # must be imported before docutils
import docutils
from docutils import parsers, utils, frontend


class RstParserTests(unittest.TestCase):

    def test_inputrestrictions(self):
        parser_class = parsers.get_parser_class('rst')
        parser = parser_class()
        document = utils.new_document('test data', frontend.OptionParser(
                    components=(parser, )).get_default_values())

        if sys.version_info < (3, 0):
            # supplying string input is supported, but only if ascii-decodable
            self.assertRaises(UnicodeDecodeError,
                              parser.parse, b'hol%s' % chr(224), document)
        else:
            # input must be unicode at all times
            self.assertRaises(TypeError, parser.parse, b'hol', document)


if __name__ == '__main__':
    unittest.main()
