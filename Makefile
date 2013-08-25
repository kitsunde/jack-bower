develop:
	pip install "file://`pwd`#egg=bower"
	pip install -e .


release:
	python setup.py sdist upload
