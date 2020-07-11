from fabric import task
import os

pbook = ".." + os.path.sep + "playbooks" + os.path.sep + "banner.yaml"

@task
def configureLoginMotd(c, device):
    c.put(pbook, remote = f"/home/{c.user}")
    c.run(f"ansible-playbook banner.yaml -e device={device}")