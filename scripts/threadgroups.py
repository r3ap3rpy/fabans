from fabric import ThreadingGroup as tg

def tshoot(c):
    print(f"Checking os version")
    c.run('uname -s')
    print(f"Checking free space")
    c.run('df -h')
    print(f"Checking uptime")
    c.run('uptime')

g = tg('centos','ubuntu','fedora')

tshoot(g)