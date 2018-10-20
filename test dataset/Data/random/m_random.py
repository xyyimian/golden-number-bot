import random
with open('random.txt','w') as f:
	for i in range(400):
		l = ""
		for j in range(8):
			l += str(random.random()*100) + '\t'
			
		f.write(l +'\n')
			