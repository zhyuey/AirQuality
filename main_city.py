import datetime
import os
import sys
###########################################
#  if having two arguments, do not download new file, use existed file instead
#  I do this due to accelerate the development process
#
if len(sys.argv) < 2:
    use_existFile = False
else:
    if int(sys.argv[1])>0:
        use_existFile = True
    else:
        use_existFile = False


dt = datetime.datetime.now()

if not os.path.exists('./database_city'):
    os.mkdir(r'./database_city')

dtstr = dt.strftime("./database_city/%Y-%m-%d-%H-%M")
if not use_existFile:
    filename = dtstr + ".txt"
    cmd1 = "python3 air_city.py " + filename
    os.system(cmd1)

    namefile = open("filename_city.txt", "w")
    namefile.write(filename)
    namefile.close()
else:
    namefile = open("filename_city.txt", "r")
    filename = namefile.read()
    namefile.close()

xmlname = dtstr + ".xml"
cmd2 = "python3 ./python-wcfbin-master/wcf2xml.py " + filename + " >" + xmlname
os.system(cmd2)


cmd3 = "python3 process_city.py " + xmlname
os.system(cmd3)





