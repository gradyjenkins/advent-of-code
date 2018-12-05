import unittest

from day_one_part_one import add

class AddTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(['+1', '+1', '+1']), 3)
        self.assertEqual(add(['+1', '+1', '-2']), 0)
        self.assertEqual(add(['-1', '-2', '-3']), -6)

