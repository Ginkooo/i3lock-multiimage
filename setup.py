#!/usr/bin/env python3

import config
import subprocess

install_to = config.INSTALL_FOLDER

subprocess.check_call('cp -r . {}'.format(install_to), shell=True)

with open('/usr/local/bin/lock', 'w') as f:
    f.write('cd %s\n' % install_to)
    f.write('./lock.py')

subprocess.check_call('chmod 755 /usr/local/bin/lock', shell=True)
