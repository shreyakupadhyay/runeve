#!/usr/bin/env python
'''
Author : Shreyak Upadhyay
Email : shreyakupadhyay07@gmail.com
Subject : running programs of various languages using one script .
Description: Using system calls and various python libraries compiling programs of various programming langauges using on single
script of python. 
'''

import sys , os ,optparse
from subprocess import call

array = []
update=0
array= sys.argv[1]
for j in range(0,len(array)):
    if(array[j] == '.'):
        update=j


arr = array[update:len(array)+1]


def compiler(compiler_name):  #give compiler name as a string like "gcc" for C or "g++" for c++
    parser = optparse.OptionParser()
    parser.add_option('-n', '--executable', dest='file', help='file name')
    (options, args) = parser.parse_args()

    if options.file is None:
        options.file=raw_input("Give the name of executable file: ")
        call([compiler_name ,sys.argv[1], "-o",options.file])
        call(["./"+options.file])
        

    else:
        call([compiler_name ,sys.argv[1], "-o",sys.argv[3]])
        call(["./"+sys.argv[3]])
        os.remove(sys.argv[3])

if(arr[1]=='c'):  #for C language
    compiler("gcc")


elif(arr[1]=='c' and arr[2]=='p' and arr[3]=='p'):  #for C++ language
    compiler("g++")



elif(arr[1]=='p' and arr[2]=='y'):  #for python language
    call(["python",sys.argv[1]])

elif(arr[1]=='p' and arr[2]=='h' and arr[3]=='p'):  #for php language
    call(["php",sys.argv[1]])


elif(arr[1]=='j' and arr[2]=='s'): #for javascript language
    call(["node",sys.argv[1]])


elif(arr[1]=='r' and arr[2]=='b'):  #for ruby language
    call(["ruby",sys.argv[1]])  
    
