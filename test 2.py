import os
import sys


'''file = open("/Volumes/aj/hello world.txt", 'w')
x = 1

while True:
    x = x + 1
    print(x)
    file.write(str(x))
    file.flush()
   # file.close()'''


import sys
oldstdout = sys.stdout     # So you can restore later
sys.stdout = open("/Volumes/aj/hello world.txt", 'w')  # Or whatever your logfile is
for i in range(10):
    print ("Hello", i)
sys.stdout.close()
sys.stdout = oldstdout