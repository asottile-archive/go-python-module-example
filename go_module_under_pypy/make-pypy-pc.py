#!/usr/bin/env pypy
from __future__ import unicode_literals

import argparse
import distutils.sysconfig
import io
import os.path


PC_FILE = '''\
Name: pypy
Description: pypy
Version: 0
Cflags: -I{includedir}
Libs: -L{libdir} -lpypy-c
'''


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('destination')
    args = parser.parse_args()

    with io.open(args.destination, 'w') as pc_file:
        pc_file.write(PC_FILE.format(
            includedir=distutils.sysconfig.get_python_inc(),
            libdir=os.path.join(distutils.sysconfig.EXEC_PREFIX, 'bin'),
        ))


if __name__ == '__main__':
    exit(main())
