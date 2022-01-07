import signal
import os

class TimeoutException(Exception):
        pass

def handler(signum,frame):
        raise TimeoutException()

def cron():
    signal.signal(signal.SIGALRM,handler)
    signal.alarm(3)
    
try:
        cmd = os.popen("%s/%s 2> %s" %(cron_dir,script,f)).read().strip()
except:
        logger.error("%s script timeout" %script)