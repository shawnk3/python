import cmd,sys,cv2
from cv2 import *

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return map( arg.split())

def circle(arg):
    return cv2.circle(*arg)

class Paint(cmd.Cmd):
    global cam,canvas
    cam = cv2.VideoCapture(0)
    _,canvas = cam.read()
    cam.release()
    cv2.waitKey(0)
    intro = 'Welcome to the Paint app. Press ? for commands'
    prompt = '>'
    file = None
    

    
    
    def do_circle(self,arg):
        ##circle(*parse(canvas, arg))
        cv2.imshow('Canvas',canvas)
        print("Press q to quit")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        
    def do_bye(self, arg):
        'close the window, and exit:  BYE'
        print('Thank you for using Paint app.')
        self.close()
        bye()
        return True
    
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

paint = Paint()
paint.cmdloop()