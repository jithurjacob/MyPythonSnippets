alph=['a','b','c','d']
num=[1,2,3,4,5,6,7]
try:
	print alph
	alph=alph+[True]
	print (alph[:],len(alph))
	alph.append(num)
	print (alph,len(alph))
	alph.extend(num)
	print (alph,len(alph))
	alph.insert(1,'f')
	print (alph,len(alph))
	print (1,alph.count(1))
	print 1 in alph
	print alph.index(1)
	alph.remove(3)
	print alph
	del alph[1]
	print alph
	print alph.pop(-2)
	if alph:
		print "yes"
except Exception, e:
	raise e


'''def hi():
 print "hi"

print hi()"hi"'''