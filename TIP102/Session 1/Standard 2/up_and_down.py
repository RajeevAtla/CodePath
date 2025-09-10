def up_and_down(lst):
	odds = 0
	evens = 0
	for num in lst:
		if num % 2 == 0:
			evens += 1
		else:
			odds += 1
	return odds - evens


lst = [1, 2, 3]
print(up_and_down(lst))

lst = [1, 3, 5]
print(up_and_down(lst))

lst = [2, 4, 10, 2]
print(up_and_down(lst))
