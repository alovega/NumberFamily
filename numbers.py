

class NumberFamily(object):
	def __init__(self, a, b):
		"""

		:param a:indicates the number of even numbers needed
		@:type: int
		:param b:indicates the number of odd numbers needed
		@type: int
		"""
		self.a = a
		self.b = b

	# code to generate a list of even and odd numbers
	# depending on the input given

	def generate_list(self):
		"""
		:param self:
		:return: returns an integer of all possible array combinations
		"""

		generated_list = []
		if self.a:
			i = 1
			n = 2
			while i <= self.a:
				generated_list.append(n)
				n += 2
				i += 1
		if self.b:
			j = 1
			n = 1
			while j <= self.b:
				generated_list.append(n)
				n += 2
				j += 1

		for i in generated_list:
			x = NumberFamily.subsequences(NumberFamily.generate_even_or_odd_list(i), 0, [])

		return x

	# code to return all possible
	# subsequences of length 2 or greater for given array using
	# recursion

	# Recursive function to return all
	# possible subsequences for given array
	@staticmethod
	def subsequences(arr, index, subarr, a = []):
		"""
		:param arr: the array to use while generating sub arrays
		:param index: the starting index
		:param subarr: holder for an empty list of sub arrays
		:param a: the list to return
		:return: returns a list of sub arrays
		"""
		# Print the subsequence when reach
		# the leaf of recursion tree
		if index == len(arr):
			# Condition to avoid printing
			# empty subsequence
			if len(subarr) >= 2:
				if not all(n % 2 == 1 for n in subarr) and not all(n % 2 == 0 for n in subarr):
					a.append(subarr)

		else:
			# Subsequence without including
			# the element at current index
			NumberFamily.subsequences(arr, index + 1, subarr)

			# Subsequence including the element
			# at current index
			NumberFamily.subsequences(arr, index + 1, subarr + [arr[index]])

		return a

	@staticmethod
	def generate_even_or_odd_list(n):
		if n % 2 == 0:
			x = [i for i in range(n) if i % 2 !=0]
			x.append(n)
			return x
		else:
			x = [i for i in range(1, n) if i % 2 == 0]
			x.append(n)
			return x

