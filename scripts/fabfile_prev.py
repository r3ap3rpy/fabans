from fabric import task,Config
import os
sources = ('..' + os.path.sep + 'sources' + os.path.sep)

@task
def uptime(c):
    print(f"Getting uptime from host: {c.host}")
    c.run('uptime')

@task
def tshoot(c):
    print(f"Checking os version on :{c.host}")
    c.run('uname -s')
    print(f"Checking free space on :{c.host}")
    c.run('df -h')
    print(f"Checking uptime on :{c.host}")
    c.run('uptime')

@task
def uploadDocs(c):
    print(f"Working on host: {c.host}")
    c.sudo('yum install unzip -y')
    c.put(f"{sources + 'fabric-2.5.zip'}",remote = f'/home/{c.user}/')
    c.run(f"unzip -o /home/{c.user}/fabric-2.5.zip")
    c.run(f"rm -f /home/{c.user}/fabric-2.5.zip")
    