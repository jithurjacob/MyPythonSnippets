# https://www.hackerrank.com/challenges/nested-list?h_r=next-challenge&h_v=zen
N = input()
students = []
#students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

for i in xrange(N):
	name = raw_input()
	mark = input()
	students.append([name,mark])

import operator
students = sorted(students,key=operator.itemgetter(0))
secondLowest = sorted(set([student[1] for student in students]))[1]
for student in students:
	if student[1] == secondLowest:
		print student[0]
