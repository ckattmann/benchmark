import time

class benchmark(object):
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        self.starttime = time.time()
    def __exit__(self, typ, value, traceback):
        print(str(self.name)+'\t: '+str(time.time()-self.starttime))
        return False
