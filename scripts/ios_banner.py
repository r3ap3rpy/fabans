from fabric import Connection
import os


c = Connection('centos')

device = 'c7200'

pbook = ".." + os.path.sep + "playbooks" + os.path.sep + "banner.yaml"

c.put(pbook, remote = f"/home/{c.user}")
c.run(f"ansible-playbook banner.yaml -e device={device}")