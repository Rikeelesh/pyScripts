from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
#pip install watchdog
import os
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self,event):
        for filename in os.listdir(folder_to_track):
            file_name,file_extension = os.path.splitext(filename)
            if file_extension in ['.jpg','.png']: #check for picture extension
                src = folder_to_track +"/"+filename
                new_destination = folder_Images +"/"+filename
                os.rename(src,new_destination)
            elif file_extension == '.exe': #check for apps extension
                src = folder_to_track +"/"+filename
                new_destination = folder_Apps +"/"+filename
                os.rename(src,new_destination)
            elif file_extension == '.pdf': #check for pdf extension
                src = folder_to_track +"/"+filename
                new_destination = folder_PDF +"/"+filename
                os.rename(src,new_destination)
            else: #put in root folder if none of above
                src = folder_to_track +"/"+filename
                new_destination = folder_destination +"/"+filename
                os.rename(src,new_destination)


folder_to_track ='' #uri of root folder
folder_Images ='' #uri of Images folder
folder_destination =' ' #uri of destination folder
folder_Apps = ' ' #uri of Apps folder
folder_PDF = ' ' #uri of PDF folder

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler,folder_to_track,recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)

except KeyboardInterrupt:
    observer.stop()
observer.join()
