def get_odds(nums):
	return [num for num in nums if num % 2 != 1]

nums = [1, 2, 3, 4]
get_odds(nums)

nums = [2, 4, 6, 8]
get_odds(nums)
