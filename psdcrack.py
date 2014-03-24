#!/usr/bin/python
#
# linux root password cracker
#
#
import crypt

def testPass(cryptPass):
	cryptMode = cryptPass[0:3]
	if cryptMode == '$6$':
		salt = '$6$' + cryptPass.split('$')[2]
	dictFile = open('dictionary.txt', 'r')
	for word in dictFile.readlines():
		word = word.strip('\n')
		cryptWord = crypt.crypt(word, salt)
		if (cryptWord == cryptPass):
			print "[+] Found Password: " + word + "\n"
			return
	print "[-] Password Not Found.\n"
	return

def main():
	passFile = open('/etc/shadow')
	for line in passFile.readlines():
		if 'root' in line:
			cryptPass = line.split(':')[1]
			break
	print 'crypt root password is : '
	print cryptPass
	testPass(cryptPass)
	

if __name__ == "__main__":
	main()















