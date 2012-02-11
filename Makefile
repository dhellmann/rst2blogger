# Default target is to show help
help:
	@echo "sdist          - Source distribution"
	@echo "html           - HTML documentation"
	@echo "docclean       - Remove documentation build files"
	@echo "upload         - upload a new release to PyPI"
	@echo "develop        - install development version"
	@echo "test           - run the test suite"
	@echo "test-quick     - run the test suite for bash and one version of Python ($(PYTHON26))"
	@echo "website        - generate web version of the docs"
	@echo "installwebsite - copy web version of HTML docs up to server"

.PHONY: sdist
sdist: html
	python setup.py sdist

# Documentation
.PHONY: html
html:
	python setup.py build_sphinx

.PHONY: docclean
docclean:
	rm -rf docs/build docs/html

installwebsite: html
	(cd build/sphinx/html && rsync --rsh=ssh --archive --delete --verbose . www.doughellmann.com:/var/www/doughellmann/DocumentRoot/docs/rst2blogger/)

# Register the new version on pypi
.PHONY: register
register:
	echo "USE upload target"
	exit 1
	python setup.py register

.PHONY: upload
upload:
	python setup.py sdist upload

# Testing
test:
	tox

test-quick:
	tox -e py27

develop:
	python setup.py develop
