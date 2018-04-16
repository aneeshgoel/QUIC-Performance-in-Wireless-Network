import time
import speedtest
import subprocess

localtime = time.asctime( time.localtime(time.time()) ).split()[3] 

print "Beginning Jio Speed Test at time", localtime,"\n"

while(1):
	localtime = time.asctime( time.localtime(time.time()) ).split()[3] 
	if (int(localtime.split(":")[1]) %10 == 0):
		
		#print "\nAt time", localtime.split(":")[0],":",localtime.split(":")[1]
		subprocess.Popen("date")
		subprocess.Popen("speedtest-cli")
		#print"Done with one iteration\n"
		time.sleep(60)
	else:
		#print int(localtime.split(":")[1]), "\n"
		time.sleep(2)
