import re
T=input()
for x in range(0,T):
	s=raw_input();
	N=len(s)
	print str(len(re.sub(r'(www\.)|[aeiou]',"",s))+1)+"/"+str(N)
	