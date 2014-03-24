#!/usr/bin/python
#
# linux root password cracker
#
#
import crypt

f = open('/etc/shadow', 'r')
for i in f:
        if 'root' in i:
        s = i
        break
shadow = s.split(":")[1]
print "root:"
print shadow
mode = shadow[0:3]
        if mode == "$6$":
        print "Sha1-512 crypt"
        salt = "$6$" + shadow.split("$")[2]
        password = 'ThisIsPassword'
        result = crypt.crypt(password, salt)
        print result
