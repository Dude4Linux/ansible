#!/usr/bin/python
# Copyright (c) 2010 Alon Swartz <alon@turnkeylinux.org>
# Added ssh keygen using same password. 2013 John Carver <dude4linux@gmail.com>
"""Set account password and generate ssh key

Arguments:
    username      username of account to set password for

Options:
    -p --pass=    if not provided, will ask interactively
"""

import sys
import getopt
import subprocess
from subprocess import PIPE
import signal

from dialog_wrapper import Dialog

def fatal(s):
    print >> sys.stderr, "Error:", s
    sys.exit(1)

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s <username> [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "hp:", ['help', 'pass='])
    except getopt.GetoptError, e:
        usage(e)

    if len(args) != 1:
        usage()

    username = args[0]
    password = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt in ('-p', '--pass'):
            password = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "%s Password" % username.capitalize(),
            "Please enter new password for the %s account." % username)


    command = ["chpasswd"]
    input = ":".join([username, password])

    p = subprocess.Popen(command, stdin=PIPE, shell=False)
    p.stdin.write(input)
    p.stdin.close()
    err = p.wait()
    if err:
        fatal(err)

    subprocess.call(['su', username, '-c', 'ssh-keygen -q -b 4096 -t rsa -f $HOME/.ssh/id_rsa -N %s' % password])
    if err:
        fatal(err)

if __name__ == "__main__":
    main()

