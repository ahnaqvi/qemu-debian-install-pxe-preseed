import pexpect

# get password from root file after installation


child = pexpect.spawn("./boot.sh")
child.expect('login: ')
child.expect('Password: ')
child.expect('~#')