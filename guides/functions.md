### Functions

Fabric allows you to group series of commands together and call upon them when needed.
The corresponding video of the course helps you with that.

Here is a boiler plate template.

``` python
from fabric import Connection

management = Connection('server')

def myfunction(c):
    c.run('mycommand')
    c.get('mmyfile')

myfunction(management)
```

This script *functions.py* should be checked out for reference.