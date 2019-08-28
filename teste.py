import random
import string
#def randomString(stringLength=10):
args=[]
for i in range(1,10):
	letters = string.ascii_lowercase
	#print (random.choice(letters))
	args.append(random.choice(letters))
print (args)
#return ''.join(random.choice(letters) for i in range(10))
#print ("Random String is ", randomString() )