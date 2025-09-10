def running_sum(superhero_stats):
	ans = []
	for i in range(len(superhero_stats)):
		if i == 0:
			ans.append(superhero_stats[i])
		else:
			ans.append(ans[i-1] + superhero_stats[i])
	return ans

superhero_stats = [1, 2, 3, 4]
print(running_sum(superhero_stats))

superhero_stats = [1, 1, 1, 1, 1]
print(running_sum(superhero_stats))

superhero_stats = [3, 1, 2, 10, 1]
print(running_sum(superhero_stats))
