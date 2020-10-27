mass = [5,8,9,4,8,3,7,4]
m = {}
for i in mass:
	if i in m:
		m[i] += 1
		print ("Повторяющееся число:" , i)
	else:
		m[i] = 1