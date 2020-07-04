from fabric import Connection
import argparse

parser = argparse.ArgumentParser('This is a simple argparse demo!')
parser.add_argument('-host','--host', type = str, help = "The host to bother")
args = parser.parse_args()

if not args.host:
    parser.print_help()
else:
    print(f"Running against host: {args.host}")

c = Connection(args.host)

c.run('uptime')