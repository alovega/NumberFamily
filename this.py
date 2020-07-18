from itertools import combinations

def get_even(size):
	start = 1
	even = []
	while len(even) < size:
		if start % 2 == 0:
			even.append(start)
			start += 1
		else:
			start+=1
	return even

def get_odd(size):
	start = 0
	odd = []
	while len(odd) < size:
		if start % 2 != 0:
			odd.append(start)
			start += 1
		else:
			start+=1
	return odd

def invalid(numbers, even_list, odd_list):
	invalid = False
	if numbers[0] in odd_list:
		for i in numbers[1:]:
			if i in odd_list:
				invalid = True
	if numbers[0] in even_list:
		for i in numbers[1:]:
			if i in even_list:
				invalid = True
	return invalid


def possible_photos(E,O):
	all_combinations = []
	new_combinations = []
	even_list = get_even(E)
	odd_list = get_odd(O)
	t_list = (even_list + odd_list)
	t_list.sort(reverse=True)
	for i in range(1, len(t_list) + 1 ):
		for subset in combinations(t_list, i):
			if len(subset) > 1:
				if not(invalid(subset, even_list, odd_list)):
					all_combinations.append(subset)


	return set(all_combinations)


print(possible_photos(2,4))
