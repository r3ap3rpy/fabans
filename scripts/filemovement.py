from fabric import Connection,Config
import os

sources = ('..' + os.path.sep + 'sources' + os.path.sep)
config = Config(overrides={'sudo':{'password':f'fabric\n'}})

c = Connection('centos',config = config)
c.sudo('yum install unzip -y')
c.put(f"{sources + 'fabric-2.5.zip'}",remote = f'/home/{c.user}/')
c.run(f"unzip -o /home/{c.user}/fabric-2.5.zip")
c.run(f"rm -f /home/{c.user}/fabric-2.5.zip")
c.get(f"/home/{c.user}/a.txt")
c.get(f"/home/{c.user}/b.txt")