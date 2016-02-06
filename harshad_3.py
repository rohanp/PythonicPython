#!/usr/bin/env python3
""" Harshad Number Problem """
__author__ = "Rohan Pandit"

def is_harshad(n):

	assert(isinstance(n, int))

    if n % sum_digits(n) == 0 :
		return True
	else:
		return False

class TestMethods(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(is_harshad(5), True)

    def test_double_digit(self):
        self.assertEqual(is_harshad(12), True)

	def test_false(self):
		self.assertEqual(is_harshad(11), False)

    def test_not_integer(self):
        with self.assertRaises(TypeError):
                is_harshad("hi")


if __name__ == "__main__":
	unittest.main()
