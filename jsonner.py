def JSONner(x):
	if isinstance(x, int):
			return str(x)
	elif isinstance(x, basestring):
			return '"%s"' %x
	elif isinstance(x, list):
		new_string = "["
		for el in x:
			new_string +=JSONner(el) + ", "
		new_string = new_string[:-2]
		new_string += "]"
		return new_string
	elif isinstance(x, dict):
		new_string = "{"
		for key in x:
			new_string += "%s" % key + ":" + JSONner(x[key]) + ", "
		new_string = new_string[:-2]
		new_string += "}"
		return new_string


print JSONner([{"foo": [1, "foo"]}, ["foo", 5], 5])