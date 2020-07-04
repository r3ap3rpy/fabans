from fabric import Connection

c = Connection('centos')

result = c.run('sudo yum install nano -y')