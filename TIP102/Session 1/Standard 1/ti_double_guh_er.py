def tiggerfy(s):
	return ''.join([char for char in s if char not in 'tigerTIGER'])

s = "suspicerous"
tiggerfy(s)

s = "Trigger"
tiggerfy(s)

s = "Hunny"
tiggerfy(s)
