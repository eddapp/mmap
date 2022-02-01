from pathlib import Path
import os
import datetime
import logging
import hashlib
import subprocess


class paths:        
    def __init__(self):
        return

    def get_service():
        return self.get_service

    def get_application():
        return self.get_application

    def get_event():
        return self.get_event

    def get_system():
        return self.get_system




#path to exec script
map_paths = subprocess.run(["~/Desktop/lesson_one/final_projext/marmap/maraudersMap.sh"], shell=True)





class service(paths):
    
    # retun serivce paths from bash script 
    def get_service(self):
        return map_paths.get_service(self)
        

class application(paths):
    
       
    # retun application paths from bash script     
    def get_application(self):
        return map_paths.get_application(self)


class event(paths):
    
               
    # retun event paths from bash script 
    def get_event(self):
        return map_paths.get_event(self)


class system(paths):
    
        
    # retun system paths from bash script      
    def get_system(self):
        return map_paths.get_system(self)