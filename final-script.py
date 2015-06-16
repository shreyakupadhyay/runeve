import sys
import os
shreyak = os.path.isfile(sys.argv[2])
if (shreyak == False):
	filename = raw_input("Write the last name here again: ")
	target = open (filename, 'a')
	line1 = sys.argv[1]
	target.write(line1)
	print "we have added the "+ sys.argv[1] +" name to the file " + filename
	target.close()
else:
	print sys.argv[2]+ " this file already exists"

file = open(sys.argv[2],"rw+")
file.seek(0)
count=0
arr = []
j = 0
for i in file.read():
	if (i == '.'):
		count=1
	if (count ==1):
		arr.append(i)
		j=j+1;
for k in range(0,len(arr)):
	print arr[k]
file.close()
if(arr[1]=='c'):
	exe=raw_input("Give the name of executable file: ")
	import sys
	from subprocess import call
	call(["gcc" ,sys.argv[1], "-o",exe])
	call(["./"+exe])


elif(arr[1]=='p' and arr[2]=='y'):
	import sys
	from subprocess import call
	call(["python",sys.argv[1]])

elif(arr[1]=='p' and arr[2]=='h' and arr[3]=='p')
	import sys
	from subprocess import call
	call(["php",sys.argv[1]])


elif(arr[1]=='j' and arr[2]=='s')
	import sys
	from subprocess import call
	call(["node",sys.argv[1]])


elif(arr[1]=='r' and arr[2]=='b')
	import sys
	from subprocess import call
	call(["ruby",sys.argv[1]])	
	
