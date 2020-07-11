from fabric import task
import os

pbook = ".." + os.path.sep + "playbooks" + os.path.sep + "tshoot.yaml"

@task
def tshoot(c, Device):
    c.put(pbook, remote = f"/home/{c.user}")
    c.run(f"ansible-playbook tshoot.yaml -e device={Device}")