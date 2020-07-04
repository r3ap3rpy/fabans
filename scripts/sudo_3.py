from fabric import Connection, Config
from getpass import getpass

sudopwd = getpass('Whats the sudo password: ')

config = Config(overrides={'sudo':{'password':f'{sudopwd}\n'}})

c = Connection('centos', config = config)

c.sudo('whoami', pty = True)
c.run('whoami')
