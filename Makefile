.PHONY: build
build:
	python3 -m build
.PHONY: upload
upload: build
	#python3 -m twine upload --repository testpypi dist/*
	python3 -m twine upload dist/*