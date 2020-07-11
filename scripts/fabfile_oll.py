from fabric import task

@task
def deployUser(c, Machine, User, Pass):
    if not c.host or not User or not Pass:
        print("We need a host a user and a password!")
    else:
        print(f"Deploy user: {User} on host: {Machine} with pass: {Pass}")
        c.put("..\\playbooks\\proxy_user.yaml", remote = f"/home/{c.user}/")
        c.run(f"ansible-playbook /home/fabric/proxy_user.yaml -e FQDN={Machine} -e user='{User}' -e password='{Pass}'")