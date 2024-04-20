import time
import os
import shutil


path = '' 
days = 30  

seconds = days * 24 * 60 * 60

if os.path.exists(path):
    for root, dirs, files in os.walk(path):
        for name in files + dirs:
            file_path = os.path.join(root, name)
            
            ctime = os.stat(file_path).st_ctime
            
            if time.time() - ctime > seconds:
                
                if os.path.isfile(file_path):
                    os.remove(file_path)
                else:
                    shutil.rmtree(file_path)
else:
    print("Path not found.")