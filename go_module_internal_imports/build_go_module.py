#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals

import contextlib
import distutils.sysconfig
import os.path
import pipes
import shutil
import subprocess
import sys
import tempfile


PYPY = '__pypy__' in sys.builtin_module_names


@contextlib.contextmanager
def tmpdir():
    tempdir = tempfile.mkdtemp()
    try:
        yield tempdir
    finally:
        shutil.rmtree(tempdir)


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


def print_cmd(env, cmd):
    print('$ {}'.format(' '.join(
        ['{}={}'.format(k, pipes.quote(v)) for k, v in env.items()] +
        [pipes.quote(p) for p in cmd]
    )))


def main():
    pkg_path = 'github.com/asottile/foo'
    main_file = 'hello_lib/main.go'
    with tmpdir() as tempdir:
        # Copy our source to a temporary GOPATH
        copy_path = os.path.join(tempdir, 'src', pkg_path)
        # Not all, copytree depends on directory *not* existing
        os.makedirs(os.path.dirname(copy_path))
        shutil.copytree(os.getcwd(), copy_path)
        path = os.path.join(copy_path, os.path.dirname(main_file))

        cflags = '-I{}'.format(distutils.sysconfig.get_python_inc())
        ldflags = get_ldflags()

        env = {'CGO_CFLAGS': cflags, 'CGO_LDFLAGS': ldflags, 'GOPATH': tempdir}

        cmd_get = ('go', 'get')
        print_cmd(env, cmd_get)
        subprocess.check_call(cmd_get, env=dict(os.environ, **env), cwd=path)

        cmd_build = (
            'go', 'build', '-buildmode=c-shared', '-i', '-o',
            os.path.abspath(so_file_name('hello_lib')),
        )
        print_cmd(env, cmd_build)
        subprocess.check_call(cmd_build, env=dict(os.environ, **env), cwd=path)


if __name__ == '__main__':
    exit(main())
