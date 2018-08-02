from threading import Thread
from pinkybot.monitor import pinkybot
class imonitor(Thread):
    def __init__(self,loginParams):
        Thread.__init__(self)
        self.daemon = True
        self.loginParams=loginParams
        
        self.start()
    def run(self):
        login= pinkybot()
        login.mypinkylogin(self.loginParams)
        

class myClassB(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            print ('B')

