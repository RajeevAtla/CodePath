def split_haycorns(quantity):
	ans = []
	
	for i in range(1, quantity+1):
		if quantity % i == 0:
			ans.append(i)
	return ans

quantity = 6
split_haycorns(quantity)

quantity = 1
split_haycorns(quantity)
