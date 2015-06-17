import sys
import os
from subprocess import call

array = []
update=0
array= sys.argv[1]
for j in range(0,len(array)):
	if(array[j] == '.'):
		update=j

u=0
arr = []

arr = array[update:len(array)+1]




if(arr[1]=='c'):
	exe=raw_input("Give the name of executable file: ")
	call(["gcc" ,sys.argv[1], "-o",exe])
	call(["./"+exe])
	os.remove(exe)

elif(arr[1]=='p' and arr[2]=='y'):
	call(["python",sys.argv[1]])

elif(arr[1]=='p' and arr[2]=='h' and arr[3]=='p'):
	call(["php",sys.argv[1]])


elif(arr[1]=='j' and arr[2]=='s'):
	call(["node",sys.argv[1]])


elif(arr[1]=='r' and arr[2]=='b'):
	call(["ruby",sys.argv[1]])	
	
