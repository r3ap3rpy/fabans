from fabric import Connection

def tshoot(c):
    print(f'Checking free space on :{c.host}')
    c.run('df -h')
    print(f"Checking uptime on: {c.host}")
    c.run('uptime')

for host in ('centos','ubuntu'):
    c = Connection(host)
    tshoot(c)