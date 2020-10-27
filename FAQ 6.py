mass = [1,9,7,1,3,7,4,5]
s = set()
m = []
for i in mass:
	if i in s:
		continue
	s.add(i)
	m.append(i)
print(m)