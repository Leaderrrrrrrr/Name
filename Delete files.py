
import os, glob

filelist = glob.glob(os.path.join("Data", "*"))
for f in filelist:
    os.remove(f)
 
