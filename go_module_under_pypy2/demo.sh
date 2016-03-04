#!/usr/bin/env bash
set -ex
make
pypy -c 'import sum; print(sum.sum(1, 2))'
