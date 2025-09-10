def find_villain(crowd, villain):
	return [index for index, person in enumerate(crowd) if person == villain]


crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
find_villain(crowd, villain)
