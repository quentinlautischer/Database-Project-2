from rgxHandler import *

class phase1:

	def 


rgx = rgxHandler()
f = open("sample10.text")

linesout = []

i = 0
k = 0

for line in f:
	#li = (line.strip('\n'))
	if i == 0:
		linesout.append(str(k + 1) + ',')
		linesout.append(rgx.line_rgx(line) + ',')
		i+=1
	elif i in [1, 3, 4, 6, 7, 8]:
		linesout.append(rgx.line_rgx(line) + ',')
		i+=1
	elif i in [2, 5, 9]:
		if i == 9:
			linesout.append('"' + rgx.line_rgx(line) + '"')
		else:
			linesout.append('"' + rgx.line_rgx(line) + '"' + ',')
		i+=1
	else:
		i=0
