#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals

import distutils.sysconfig
import os.path
import pipes
import subprocess
import sys


PYPY = '__pypy__' in sys.builtin_module_names


def so_file_name(mod):
    if PYPY:  # pragma: no cover
        return '{}.pypy-{}{}.so'.format(mod, *sys.pypy_version_info[:2])
    else:
        return '{}.so'.format(mod)


def get_ldflags():
    if PYPY:
        return '-L{} -lpypy-c'.format(
            os.path.dirname(os.readlink(sys.executable)),
        )
    else:
        return distutils.sysconfig.get_config_var('BLDLIBRARY')


def main():
    cflags = '-I{}'.format(distutils.sysconfig.get_python_inc())
    ldflags = get_ldflags()
    cmd = ('go', 'build', '-buildmode=c-shared', '-o', so_file_name('sum'))
    env = {'CGO_CFLAGS': cflags, 'CGO_LDFLAGS': ldflags}
    print(
        '$ {} {}'.format(
            ' '.join(
                '{}={}'.format(k, pipes.quote(v))
                for k, v in sorted(tuple(env.items()))
            ),
            ' '.join(pipes.quote(p) for p in cmd),
        ),
        file=sys.stderr,
    )
    subprocess.check_call(cmd, env=dict(os.environ, **env))


if __name__ == '__main__':
    exit(main())
