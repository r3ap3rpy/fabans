from fabric import SerialGroup

sg = SerialGroup('centos','ubuntu')

def tshoot(c):
    print(f"Checking os version on :{connection.host}")
    c.run('uname -s')
    print(f"Checking free space on :{connection.host}")
    c.run('df -h')
    print(f"Checking uptime on :{connection.host}")
    c.run('uptime')

for connection in sg:
    tshoot(connection)