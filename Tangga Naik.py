blank = ""
x=int(input())
i=x
z=0
while i>=0:
	j=i
	while j>0:
		blank=blank+"   "
		j=j-1
	kanan=1
	while kanan<(x-(i-1)):
		blank=blank+" "+str(z)+" "
		kanan=kanan+1		
		
	blank=blank+"\n"
	i=i-1
	z=z+1
print(blank)