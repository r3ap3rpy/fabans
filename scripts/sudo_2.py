from invoke import Responder
from fabric import Connection
from getpass import getpass

sudopwd = getpass('Whats the sudo password: ')

c = Connection('centos')

sudopass = Responder(pattern=f'\[sudo\] password for {c.user}:', response = f'{sudopwd}\n')

result = c.run('sudo cat /etc/sudoers',pty = True ,watchers = [sudopass])