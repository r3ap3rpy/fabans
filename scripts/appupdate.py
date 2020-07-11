from fabric import Connection

c = Connection('centos')

if c.run("which git", warn = True, hide = True).failed:
    print("Git needs to be installed!")
    c.run("sudo yum install git -y ", hide = True)
else:
    print("Git command is available!")

if c.run("test -d /home/fabric/r3ap3rpy.github.io", warn = True, hide = True).failed:
    print("The folder does not exist, cloning!")
    with c.cd("/home/fabric/"):
        c.run("git clone https://github.com/r3ap3rpy/r3ap3rpy.github.io")
else:
    print("App is already deployed, updating")
    with c.cd("/home/fabric/r3ap3rpy.github.io"):
        c.run("git pull")