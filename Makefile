
build:
	cd pypg

	# install python build package to environment.
	pip install build

	# Create distribution
	python -m build

	# Install CLI
	pip install dist/pypg-0.1.0-py3-none-any.whl



test:
	# After the install you should be able to install the packages.
	pypg test
