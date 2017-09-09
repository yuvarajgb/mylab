
import sys

def reverse(s):
	'''return the reverse of a given string'''
	rev = []
	for i in range(len(s) - 1, -1, -1):
		rev.append(s[i])

	return ''.join(rev)

def is_abecedarian(string):
	'''checks whether the given string is abecedarian'''
	if sorted(string) == list(string):
		return True
	else:
		return False

def is_triange(a, b, c):
	'''if triange  can be formed with given sides'''
	if a > (a + c) or b > (a + c) or c > (a + b):
		return False
	else:
		return True

def is_palindrome(s):
	'''check if the given string is palindrome'''
	#return s[::-1] == s
	if reverse(s) == s:
		return True
	else:
		return False


def countlines():
	'''count number of lines in a file'''
	count = 0

	with open('practise.py', 'r') as myfile:
		file = myfile.readlines()
		for line in file:
			if len(line.strip()):
				count += 1
	print "Yay, I wrote %d lines using python"%(count)
	return

def searchinfile(key):
	'''search the given string in file'''
	f = open('zippy.txt', 'r')
	file = f.readlines()
	for line in file:
		print line
		if key in line:
			return True
	return False

def searchandreplace(old, new):
	'''search a particular string and replace it with given string'''
	f = open('hosts', 'r')
	newfile = []
	file = f.readlines()
	for line in file:
		newline = line
		for each_item in line.strip().split('\t'):
			if each_item == old:
				newline = line.replace(old, new)
		print newline
		newfile.append(newline)

	fnew = open('newhosts',  'w')
	fnew.writelines(newfile)
	fnew.close()
	f.close()
	#print newfile


if __name__ == "__main__":
	'''main function'''
	
	print is_palindrome(sys.argv[1])
	#searchandreplace(old, new)
	