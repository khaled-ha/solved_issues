def encrypt(word):
	encrypt_map = {'a':0,'i':2,'o':2,'e':1,'u':3}
	hashed = []
	for i in word:
		if (i in encrypt_map.keys()):
			hashed.append(str(encrypt_map[i]))
		else:
			hashed.append(i)
	hashed.append('aca')
	coded_word = ''.join(hashed)
	return coded_word