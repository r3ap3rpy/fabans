from fabric import Connection
import os 

sources = ('..' + os.path.sep + 'sources' + os.path.sep)
pbooks = ('..' + os.path.sep + 'playbooks' + os.path.sep)
c = Connection('centos')

c.put(f"{sources + 'fabric-2.5.zip'}",remote = f'/home/{c.user}/')
c.put(f"{pbooks + 'copy.yaml'}",remote = f'/home/{c.user}/')
c.run("ansible-playbook /home/fabric/copy.yaml")