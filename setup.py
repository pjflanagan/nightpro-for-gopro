from setuptools import setup, find_packages 

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="nightpro-USERNAME",  # Replace with your own username
    version="0.0.1",
    author="Peter James Flanagan",
    author_email="pj@pjflanagan.me",
    description="A nightlapse maker for GoPro",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pjflanagan/nightpro-for-gopro",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'nightpro = nightpro.main:main'
        ]
    },
)
