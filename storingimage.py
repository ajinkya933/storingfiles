import os

# the open keyword opens a file in read-only mode by default
#f = open('/Volumes/aj/hello/hello world.txt','w')

# read all the lines in the file and return them in a list
#f.write("Foobar")
#f.close()

with open("/Volumes/aj/VLP16_Points_2017-10-24-11-21-21.bag", 'r', errors='ignore') as f:
 print (f.read())
 #f.flush()


file = open("/Volumes/untitled/sneha/aj.bag", 'w', errors='ignore')
while True:
    file.write( "/Volumes/aj/VLP16_Points_2017-10-24-11-21-21.bag")
    file.flush()
   # file.close()