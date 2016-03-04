#!/usr/bin/env bash
set -ex
make
pushd python2.7
./venv/bin/python -c 'import sum; print(sum.sum(1, 2))'
popd
pushd python3.5
./venv/bin/python -c 'import sum; print(sum.sum(1, 2))'
popd
