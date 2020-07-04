from fabric import Connection

c = Connection('centos')

def tshoot(c):
    print("We are checking the free space!")
    c.run('df -h')
    print("We are checking the uptime!")
    c.run('uptime')

def checkUser(c, user = None):
    if user:
        print(f"Checking if user: {user} exists!")
        if c.run(f'id {user}',warn = True, hide = True).failed:
            print(f"No such user: {user}")
        else:
            print(f"The user: {user} is there!")
    else:
        print(f"We need a username to check!")

tshoot(c)
checkUser(c,'fabric')