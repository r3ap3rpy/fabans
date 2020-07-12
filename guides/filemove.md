### Move files

You are able to copy to or from remote network devices with the *put* and *get* functions of your connection object.
A boiler plate template for this is the following.

``` python
from fabric import Connection

c = Connection()

c.put('localfile', remote = 'remotefolder')
c.get('remotefile')
```

You may want to check the *filemovement.py* for reference to the videos.