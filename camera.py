import cv2,cmd,sys
from cv2 import *




class Camera(cmd.Cmd):
    global cam,ch
    intro = 'Welcome to the camera shell.   Type help or ? to list commands.\n'
    prompt = '(camera) '
    file = None
    
    def do_picture(self,args):
        cam = cv2.VideoCapture(0)
        _,img = cam.read()
        cam.release()
        cv2.imshow('Image',img)
        print("Press q to quit")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def do_video(self,args):
        cam = cv2.VideoCapture(0)
        while True:
            _,img = cam.read()
            cv2.imshow('Image',img)
            ch = cv2.waitKey(1)
            print("Press q to quit") 
            if ch&0xFF == ord('q'):
                break 
        cam.release()
        cv2.destroyAllWindows()
    def do_bye(self, arg):
        'Close camera window, and exit:  BYE'
        print('Thank you for using Camera')
        self.close()
        return True
        
    
    def do_record(self, arg):
        'Save future commands to filename:  RECORD rose.cmd'
        self.file = open(arg, 'w')
    def do_playback(self, arg):
        'Playback commands from a file:  PLAYBACK rose.cmd'
        self.close()
        with open(arg) as f:
            self.cmdqueue.extend(f.read().splitlines())
    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line
    def close(self):
        if self.file:
            self.file.close()
            self.file = None  
        
camera = Camera()
camera.prompt = '>'
camera.cmdloop()

