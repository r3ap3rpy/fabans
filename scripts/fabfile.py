from fabric import task
import os
deps = ['"@Development tools"','gcc','openssl-devel','bzip2-devel','libffi-devel','zlib-devel','chkconfig']
sources = "sources"
source = (".." + os.path.sep + sources + os.path.sep + "Python-3.7.0.tgz" )
@task
def buildPython(c):
    print("Verify Python source!")
    if os.path.isfile(source):
        print("Source found")
    else:
        raise SystemExit("Source not found, aborting!")
    print(f"Copy file to destination!")
    c.put(source, remote = f"/home/{c.user}/")
    c.run(f"tar xfvz /home/{c.user}/Python-3.7.0.tgz")
    for d in deps:
        c.run(f'sudo yum install {d} -y')

    c.run(f"rm -f /home/{c.user}/Python-3.7.0.tgz")
    with c.cd(f"/home/{c.user}/Python-3.7.0/"):
        c.run('./configure --enable-optimizations --without-ensurepip --with-openssl=/usr/local/ssl')
        c.run('sudo make altinstall')
        c.run('sudo update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.7 1')
        c.run("""sudo bash -c 'echo "1"|update-alternatives --config python3'""")
            
