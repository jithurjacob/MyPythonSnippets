
t=input()
for x in xrange(0,t):
	key=raw_input()
	cipher=[i for i in raw_input()]
	key_=[]
	key_matrix=[]
	for c in key:
		if c not in key_:
			key_.append(c)
	print key_
	k=65
	key_matrix=key_
	while k<=90:
		if chr(k) not in key_:
			key_matrix.append(chr(k))
		k+=1
	print key_matrix
	k=65
	key_matrix_={}
	for i in xrange(0,26):
		dic={key_matrix[i]:chr(k+i)}
		key_matrix_.update(dic)

	print key_matrix_
	for i in xrange(0,len(cipher)):
		cipher[i]=key_matrix_.get(cipher[i])
	print "".join(cipher)
'''	
key=[0 for row in range(0,t)]
encr=[0 for row in range(0,t)]
decr=[0 for row in range(0,t)]
for i in range(0,t):
    key[i]=raw_input().strip()
    encr[i]=raw_input().strip()
for i in range(0,t):
    temp = map(str,encr[i].split())
    print(temp)
'''