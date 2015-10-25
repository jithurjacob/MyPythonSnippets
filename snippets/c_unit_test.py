from random import randint,uniform
for i in xrange(0,1000000):
	input1=randint(1,10000)
	input3=randint(1,10000)
	input2=uniform(0.0, 1.0)
	grade1=0
	grade2=0

	if (input1 > 50 and input2 < 0.7  and input3 > 5600):
		grade1=10
	elif (input1 > 50 and input2 < 0.7  ):
		grade1=9
	elif ( input2 < 0.7  and input3 > 5600):
		grade1=8
	elif (input1 > 50  and input3 > 5600):
		grade1=7
	elif (input1 > 50 or input2 < 0.7  or input3 > 5600):
		grade1=6
	else:
		grade1=5
########################################################################################
	if (input1 > 50 and input2 < 0.7  and input3 > 5600):
		grade2=10
	elif (input1 > 50 and input2 < 0.7  ):
		grade2=9
	elif ( input2 < 0.7  and input3 > 5600):
		grade2=8
	elif (input1 > 50  and input3 > 5600):
		grade2=7
	elif ((input1 > 50 and input2 >= 0.7 and input3 <= 5600)or(input1 <= 50 and input2 < 0.7 and input3 <= 5600)or(input1 <= 50 and input2 >= 0.7 and input3 > 5600)):
		grade2=6
	else:
		grade2=5

	if grade2!=grade1:
		print input1,input2,input3,grade1,grade2