def count_less_than(race_times, threshold):
	return sum(1 for time in race_times if time < threshold)

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
count_less_than(race_times, threshold)

race_times = []
threshold = 4
count_less_than(race_times, threshold)
