all: clear update build

YOLO: clear update build upload-github upload-twine sync-github

clear:
	@-rm ./dist/*

update:
	@python3 -m pip install --upgrade build
	@python3 -m pip install --upgrade pip

build:
	@python3 -m build

upload-twine:
	@python3 -m pip install --upgrade twine
	@python3 -m twine upload --repository testpypi dist/*

upload-github:
	@git add -A
	@git commit -m "yes"
	@git push
	@git pull

sync-github:
	@git pull
	@git push

