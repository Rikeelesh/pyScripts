from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
#pip install watchdog
import json
import time
import os


class MyHandler(FileSystemEventHandler):
    def on_modified(self,event):
        for filename in os.listdir(folder_to_track):
            fileName,file_extension = os.path.splitext(filename)
            if file_extension.lower() in ['.jpg','.png']: #check for picture extension
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
            elif file_extension == '.xls': #check for excel extension
                src = folder_to_track +"/"+filename
                new_destination = folder_Excel +"/"+filename
                os.rename(src,new_destination)
            elif file_extension == '.ppt': #check for excel extension
                src = folder_to_track +"/"+filename
                new_destination = folder_PowerPoint +"/"+filename
                os.rename(src,new_destination)
            elif file_extension == '.docx': #check for excel extension
                src = folder_to_track +"/"+filename
                new_destination = folder_Word +"/"+filename
                os.rename(src,new_destination)
            else: #put in root folder if none of above
                src = folder_to_track +"/"+filename
                new_destination = folder_destination +"/"+filename
                os.rename(src,new_destination)


 
os.chdir(' ') #insert your downloads folder uri

# print(os.getcwd()) #check working directory

base = ' ' #insert your downloads folder uri


folder_names = ['PDF','Images','Word','Excel','PowerPoint','Apps']

for name in folder_names:
    if not os.path.isdir(base + name):
        os.mkdir(name)
else:
    print("exists")


folder_to_track = base #uri of root folder
folder_Images = base + 'Images' #uri of Images folder
folder_destination = base  #uri of destination folder
folder_Apps = base + 'Apps' #uri of Apps folder
folder_PDF = base +'PDF' #uri of PDF folder
folder_Excel =  base + 'Excel'
folder_PowerPoint = base + 'PowerPoint'
folder_Word = base +'Word'

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