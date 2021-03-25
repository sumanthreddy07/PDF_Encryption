#import Section
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import time
import sys
import threading
import itertools

#File name and password
filename = input("Enter File Name: ")

if filename[-3:]!="pdf":
    filename += ".pdf"

if not os.path.isfile(filename):
    print("Invalid Filename / File Doesn't Exist.")
    exit()

password = input("Enter password: ")

oldfile = PdfFileReader(filename)
output = PdfFileWriter()

# 'Loading' Animation 
done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rLoading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone! File is now password protected!\n')

t = threading.Thread(target=animate)
t.start()

#Read Pages and Encrypt
for i in range(oldfile.numPages):
    page = oldfile.getPage(i)
    output.addPage(page)

output.encrypt(password)

with open("encrypted.pdf","wb") as newfile:
    output.write(newfile)
done =True