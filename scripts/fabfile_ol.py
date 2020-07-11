from fabric import task

@task
def execute(c,host,a,b):
    print(host,a,b)
    c.put(r"..\playbooks\argumented.yaml", remote = "/home/fabric/")
    c.run(f'ansible-playbook /home/{c.user}/argumented.yaml -e FQDN="{host}" -e a="{a}" -e b="{b}"')