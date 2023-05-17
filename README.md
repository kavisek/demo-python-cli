

# Python CLI

This is simple example of how to setup and build a python CLI tool called `runner`. This repo wil review how to create a simple CLI tool to download an html page and save it to a file.

## Setup Instructions

```bash
# Activate poetry environment.
cd scrapper
poetry install
poetry shell
```

You can run the CLI tool using the following command. This will invoke the `scrapper` function inside the main.py file.

Any logic within this function will be executed. You can modify this function to your liking.

```bash
# CLI Command
scrapper https://www.macrumors.com/
```

The CLI tool with then download the html page and save it to a file called `website.txt`.

But the problem with this method is that your need poetry installed on the system to run the cli tool. So we need to build the tool into a binary file.

## Build Instructions

```bash
cd ./scrapper
make build --debug
```

This will output a binary file in the `./scrapper/dist` folder. You can run this binary file on any system without the need of poetry.

You can vefify that the binary is installed with the following command.

```bash
pip list
```
You should see `scrapper 0.1.0` in the list of installed packages.

You can remove the binary with pip as well.

```bash
pip uninstall scrapper
```

### References

- https://dev.to/bowmanjd/build-command-line-tools-with-python-poetry-4mnc 
- https://pybit.es/articles/how-to-package-and-deploy-cli-apps/