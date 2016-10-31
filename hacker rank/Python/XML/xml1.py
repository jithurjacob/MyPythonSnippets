import xml.etree.ElementTree as etree
xml = ""
n = input()
for i in range(n):
	xml += raw_input()
tree = etree.ElementTree(etree.fromstring(xml))
score = 0
for child in tree.iter():
	score+=len(child.attrib)
print score

