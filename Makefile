all: clear update build

clear:
	@-rm ./dist/*

update:
	@python3 -m pip install --upgrade build
	@python3 -m pip install --upgrade pip

build:
	@python3 -m build

upload-twine:
	@python3 -m pip install --update twine
	@python3 -m twine upload --repository testpypi dist/*

upload-github:
	@git add -A
	@git commit -m "yes"
