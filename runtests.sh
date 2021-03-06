#!/bin/bash

set -o errexit

rm -rf testvenv empty unasync*.whl

python3 -m venv testvenv
source testvenv/bin/activate

pip install -U pip setuptools wheel
pip install -r dev-requirements.txt
pip wheel .

mkdir empty
cd empty

pip install ../unasynctest*.whl
INSTALLDIR=$(python -c "import os, unasynctest; print(os.path.dirname(unasynctest.__file__))")
pytest --cov="$INSTALLDIR" ../tests
