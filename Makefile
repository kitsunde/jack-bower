develop: setup-git
	pip install "file://`pwd`#egg=bower[dev]"
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
