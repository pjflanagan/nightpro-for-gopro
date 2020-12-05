
# install locally to test
install:
	python3 setup.py install 

# remove the build and dist folders
clean:
	rm -rf dist
	rm -rf build

# build the program
build:
	rm -rf dist
	rm -rf build
	python3 setup.py sdist bdist_wheel

# upload using twine
upload:
	twine upload dist/* --config-file .pypirc