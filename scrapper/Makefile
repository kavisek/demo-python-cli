
.PHONY: uninstall setup build export_requirments

export_requirments:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

setup:
	poetry install
	poetry shell

build: setup uninstall
	cd scrapper

	# install python build package to environment.
	pip install build

	# Create distribution
	python -m build

	# Install CLI
	pip install dist/scrapper-0.1.0-py3-none-any.whl


uninstall:
	pip uninstall scrapper -y