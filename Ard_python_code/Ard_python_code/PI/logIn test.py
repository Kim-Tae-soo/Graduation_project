from PythonHub import PythonHub
import time

ph = PythonHub()

ph.login()

ph.talkListen("push")

for i in range(21):
    ph.sendData()
    time.sleep(1)
