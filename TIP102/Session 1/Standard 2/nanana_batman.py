def nanana_batman(x):
	ans = ""
	
	for i in range(x):
		ans += "na"
	
	if ans == "":
		ans = "batman!"
	else:
		ans += " batman!"
	
	return ans


x = 6
print(nanana_batman(x))

x = 0
print(nanana_batman(x))
