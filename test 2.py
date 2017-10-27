import os
import sys
# the open keyword opens a file in read-only mode by default
#f = open('/Volumes/aj/hello/hello world.txt','w')

# read all the lines in the file and return them in a list
#f.write("Foobar")
#f.close()

#with open("/Volumes/untitled/sneha/ajtext.txt", 'r') as f:
# print (f.read())
 #f.flush()


# The player is allowed to keep playing as long as their power is over 0.
#x = 1
#while True:
#    x = x+1
#    print(x)


file = open("/Volumes/aj/VLP16_Points_2017-10-24-11-21-21.bag", 'w')
x = 1

while True:
    x = x + 1
    print(x)
    file.write(str(x))
    file.flush()
   # file.close()