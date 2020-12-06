
# to test locally, uninstall nightpro and then reinstall
# the local one, use check_install to check that the version
# is different
install:
	python3 setup.py install 

uninstall:
	pip3 uninstall nightpro-for-gopro

check_install:
	which nightpro
	pip3 freeze | grep nightpro

# when building the release, first remove the originals
# then run make build and make upload, then you can install using pip3
clean:
	rm -rf dist
	rm -rf build
	rm -rf nightpro_*.egg-info

build:
	python3 setup.py sdist bdist_wheel

upload:
	twine upload dist/* --config-file .pypirc