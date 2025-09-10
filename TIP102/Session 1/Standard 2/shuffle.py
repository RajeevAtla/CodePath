def shuffle(cards):
	ans = []
	first = 0
	second = len(cards)//2
	
	while second < len(cards):
		ans.append(cards[first])
		first += 1
		if second < len(cards):
			ans.append(cards[second])
			second += 1
	return ans

cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
print(shuffle(cards))

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
print(shuffle(cards))

cards = [10, 10, 2, 2]
print(shuffle(cards))
