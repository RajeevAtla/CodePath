def print_todo_list(task):
	ans = "Pooh's To Dos:"
	
	for i, item in enumerate(task):
		ans += f"\n{i+1}. {item}"
		
	return ans

task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)
