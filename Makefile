develop: setup-git
	pip install "file://`pwd`#egg=jack-bower[dev]"
	pip install -e .

setup-git:
	git config branch.autosetuprebase always
	cd .git/hooks && ln -sf ../../hooks/* ./

lint-python:
	@echo "Linting Python files"
	PYFLAKES_NODOCTEST=1 flake8 bower
	@echo ""

release:
	python setup.py sdist upload

test-py:
	django-admin.py test bower --settings=bower.tests.test_settings

test: install-test-requirements test-py

install-test-requirements:
	pip install "file://`pwd`#egg=jack-bower[tests]"
