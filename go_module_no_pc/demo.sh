#!/usr/bin/env bash
set -ex

run() {
    set -ex
    "$1" build_go_module.py
    "$1" -c 'import sum; print(sum.sum(1, 2))'
}

run pypy
run python2.7
run python3.4
run python3.5
