from subprocess import check_output
import subprocess
from threading import Thread
import time
import schedule
 
def ping(address):
    out = check_output(['ping', '-n', '5', address], timeout=30)
    print("Pinging: " + str(out))
    print(out.decode('utf-8').strip())
 
def run_threaded(ping):
    job_thread = Thread(target=ping)
    job_thread.start()

addr = input("Enter a URL (without the http part): ")
schedule.every(int(input("Enter the interval in seconds: "), 10)).seconds.do(run_threaded, ping(addr))
 
while 1:
    schedule.run_pending()
    time.sleep(1)

