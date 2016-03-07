#!/usr/bin/env bash
set -ex

run() {
    set -ex
    "$1" build_go_module.py
    "$1" -c 'import red; print(red.red(u"hi"))'
}

run pypy
run python2.7
run python3.4
run python3.5
