from fabric import Connection

c = Connection('centos')

result = c.run('cat /etc/redhat-release', hide = True)

doesitexist = c.run('test -f /proc/issue', warn = True, hide = True)

if doesitexist.failed:
    print("The file is not there!")
else:
    print("The file is there!")