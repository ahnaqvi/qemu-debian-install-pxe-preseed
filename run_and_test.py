import pexpect

child = pexpect.spawn("./boot.sh")
child.expect('login: ')
child.expect('Password: ')
child.expect('~#')