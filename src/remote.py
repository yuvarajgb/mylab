#Connect to given machine, execute a command and return the output
from __future__ import print_function
import paramiko
import subprocess

def exec_command(host, uname, password, command):
	'''executes a given command on remote machine'''
	output = ""
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		#paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG)
		ssh.connect(hostname = host, username = uname, password = password, look_for_keys = False)
		print ("Collecting command output for %s..."%(host))
		(stdin, stdout, stderr) = ssh.exec_command(command)
		
		if len(stderr.readlines()) == 0: #when  exit status is zero
			output = stdout.readlines()
			print ("Command output collected successfully!")
		
		else: #if command failed
			output = "ERRCOMMAND"
			print ("Command execution failed on %s"%(host))
   	except:
   		print ("Error connecting remote host")
   		output = "ERRHOST"
   		pass
   		#return

	return output


def pingstatus(hostname):
	'''return the status of ping status of given machine'''
	status = subprocess.call(["ping", "-c" ,"1", hostname])
	return status



if __name__ == "__main__":
	#called from main, perform following unit test
	'''
	host = "zqa-149.eng.zimbra.com"
	uname = "root"
	password = "zimbra"
	#command = 'grep \'cpu \' /proc/stat | awk \'{usage=($2+$4)*100/($2+$4+$5)} END {print usage}\''
	command = 'ls'
	output = command_executer(host, uname, password, command)
	
	if output is not None:
		print ("Command output for %s is %s"%(host, output))
	'''
	pingstatus()
	

