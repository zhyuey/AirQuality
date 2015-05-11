import datetime
import os
import sys

if len(sys.argv) < 2:
    use_existFile = False
else:
    if int(sys.argv[1])>0:
        use_existFile = True
    else:
        use_existFile = False


dt = datetime.datetime.now()

if not os.path.exists('./database'):
    os.mkdir(r'./database')

dtstr = dt.strftime("./database/%Y-%m-%d-%H-%M")
if not use_existFile:
    filename = dtstr + ".txt"
    cmd1 = "python3 air3.py " + filename
    os.system(cmd1)

    namefile = open("filename.txt", "w")
    namefile.write(filename)
    namefile.close()
else:
    namefile = open("filename.txt", "r")
    filename = namefile.read()
    namefile.close()

xmlname = dtstr + ".xml"
cmd2 = "python3 ./python-wcfbin-master/wcf2xml.py " + filename + " >" + xmlname
os.system(cmd2)


cmd3 = "python3 process.py " + xmlname
os.system(cmd3)





