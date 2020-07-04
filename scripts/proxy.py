from fabric import Connection


def tshoot(c):
    print(f"Tshooting on machine: {c.host}")
    print("Uptime on machine!")
    c.run("uptime")
    print("Free space!")
    c.run("df -h")

c = Connection('ubuntu',gateway=Connection('centos'))

#c.run('uptime')
tshoot(c)