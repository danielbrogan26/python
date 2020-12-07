#asc2.py dsb #change the range of the lool . Tru 32,129
# Change the range from (0,35) to (32,532)
for i in range (32,532):
	c = chr(i)
	print("[","=",c,"]",end="")
	if (i % 10 == 0):
		print("\n")
