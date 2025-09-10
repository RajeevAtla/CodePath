def locate_thistles(items):
	return [index for index, item in enumerate(items) if item == "thistle"]

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
locate_thistles(items)

items = ["book", "bouncy ball", "leaf", "red balloon"]
locate_thistles(items)
