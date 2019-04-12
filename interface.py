from Read import *
from Write import *
from example_search import *
from face_recognition import *
from demo_lcd import *

lcd("Scan Your Licence", 1)
t = read()

lcd("Data Found", 1)
lcd("Scan Your Finger", 1)
x, f = search()
if(f == 0):
	lcd("FingerPrint Verified", 1)
print(x)
lcd("Look AT Camera...", 1)
recog()