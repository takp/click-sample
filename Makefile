all: isort yapf flake8 mypy pytest

isort:
	isort -y -rc ./click_sample

yapf:
	yapf -i -r click_sample

flake8:
	flake8 click_sample

mypy:
	mypy click_sample

pytest:
	FRAMEWORK_DATABASE_URL=sqlite:/// USER_DATABASE_URL=sqlite:/// pytest
