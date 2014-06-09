#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Some tests for pyindex (currently just very basic tests for interleave.py)"""

import unittest
import interleave

class TestInterleave(unittest.TestCase):

    def test_interleave2(self):
        self.assertEqual(hex(interleave.interleave2(0x00, 0xFF)), '0xaaaa')
        self.assertEqual(hex(interleave.interleave2(0x0000, 0xFFFF)), '0xaaaaaaaa')

    def test_interleave3(self):
        self.assertEqual(hex(interleave.interleave3(0x00, 0xFF, 0x00)), '0x492492')
        self.assertEqual(hex(interleave.interleave3(0x0000, 0xFFFF, 0x0000)), '0x12492492')

if __name__ == '__main__':
    unittest.main()
