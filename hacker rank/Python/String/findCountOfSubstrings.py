input_str = raw_input()# "ABCDCDC"
find_str = raw_input() #"CDC"
count = 0
pos = 0
while True:
	pos = input_str.find(find_str, pos,len(input_str))
	if pos <0:
		break
	else:
		count+=1
		pos+=1
print(count)