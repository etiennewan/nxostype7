import string

xlat = [3,22,4,5,18,0,21,5,18,3,10,5,16,22,4,16,24,17,12,5,21,18,5,22,19,7]

def decrypt_type7(ep):
	pt = ""
	for i in range(len(ep)):
		x = ord(ep[i]) - xlat[i%len(xlat)]
		if ep[i] in string.ascii_lowercase:
			pt += chr(x) if chr(x) in string.ascii_lowercase else chr(x+26)
		elif ep[i] in string.ascii_uppercase:
			pt += chr(x) if chr(x) in string.ascii_uppercase else chr(x+26)
		else:
			pt += ep[i]
	return pt

def encrypt_type7(pt):
	ep = ""
	for i in range(len(pt)):
		x = ord(pt[i]) + xlat[i%len(xlat)]
		if pt[i] in string.ascii_lowercase:
			ep += chr(x) if chr(x) in string.ascii_lowercase else chr(x-26)
		elif pt[i] in string.ascii_uppercase:
			ep += chr(x) if chr(x) in string.ascii_uppercase else chr(x-26)
		else:
			ep += pt[i]
	return ep
