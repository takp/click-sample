all: isort yapf flake8 mypy pytest

isort:
	isort -y -rc ./generator

yapf:
	yapf -i -r generator

flake8:
	flake8 generator

mypy:
	mypy generator

pytest:
	FRAMEWORK_DATABASE_URL=sqlite:/// USER_DATABASE_URL=sqlite:/// pytest
