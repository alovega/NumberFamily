from unittest import TestCase

from numbers import NumberFamily


class NumberFamilyTest(TestCase):
	def setUp(self):
		self.input = NumberFamily(2, 3)

	def test_generate_list(self):
		a = self.input.generate_list()
		self.assertIsInstance(a, int)

	def test_generate_even_or_odd_list(self):
		value = self.input.generate_even_or_odd_list(4)
		self.assertIsInstance(value, list)
		self.assertEqual(value, [1, 3, 4])

	def test_generate_subsequences_input(self):
		self.input = NumberFamily(52,52)
		value = self.input.generate_list()
		self.assertEqual(value, "The input given is out of bounds")

	def test_generate_subsequences(self):
		value = self.input.subsequences([9, 8, 6, 4, 2], 0, [])
		self.assertIsInstance(value, list)

