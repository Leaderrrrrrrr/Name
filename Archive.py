
import os
import glob
import shutil
try:  
    path = os.path.join("Archive")
    os.mkdir(path)
    print("Directory '% s' created" % directory)
except:
    for file in glob.glob('Data/*'):
        print(file[18:20])
     
        if os.path.isdir("Archive/"+file[14:18]) == False:
            path = os.path.join("Archive/"+file[14:18]+"/")
            os.mkdir(path)
        if os.path.isdir("Archive/"+file[14:18]+"/"+file[18:20]) == False:
            path = os.path.join("Archive/"+file[14:18]+"/"+file[18:20]+"/")
            os.mkdir(path)
        if os.path.isdir("Archive/"+file[14:18]+"/"+file[18:20]+"/"+file[20:22]) == False:
            path = os.path.join("Archive/"+file[14:18]+"/"+file[18:20]+"/"+file[20:22]+"/")
            os.mkdir(path)
        if os.path.isfile("Archive/"+file[14:18]+"/"+file[18:20]+"/"+file[20:22]+"/"+file[6:]) == False:
            shutil.copyfile(file, "Archive/"+file[14:18]+"/"+file[18:20]+"/"+file[20:22]+"/"+file[6:])
            
        
