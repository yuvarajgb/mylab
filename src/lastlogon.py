#get the last logon time from remote machine and write to a csv file in this format: hostname, lastlogon time
#Error codes:
#ERRHOST: Error connecting host over ssh
#ERRCOMMAND: Error executing command
#DOWN: Machine is not pingable

from __future__ import print_function
import csv
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
	#main function
	username = "root"
	password = "zimbra"
	command = "last|head -1"

	for i in range(100,300): 
		hostname = "zqa-%d.eng.zimbra.com"%i
		if pingstatus(hostname) == 0:
			#check the last logon
			row = []
			row.append(hostname)#col 1

			with open("lastlogon.csv", "a") as csvfile:
				csvwriter = csv.writer(csvfile)
				output = exec_command(hostname, username, password, command)
				row.append(output)
				csvwriter.writerow(row)
		else:
			row = []
			row.append(hostname)
			row.append("DOWN")
			with open("lastlogon.csv", "a") as csvfile:
				csvwriter = csv.writer(csvfile)
				csvwriter.writerow(row)


	#EOF