.PHONY: all
all: venv

venv: Makefile
	virtualenv venv
	venv/bin/pip install pre-commit
	venv/bin/pre-commit install

.PHONY: clean
clean:
	find . -iname '*.pyc' | xargs rm -f
	rm -rf venv
