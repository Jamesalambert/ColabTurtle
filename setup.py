import setuptools

with open("README.txt", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="roverdrive-jlambert",
    version="0.5.1",
    author="James Lambert",
    #author_email="author@example.com",
    description="a turtle-like educational package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jamesalambert/ColabTurtle",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)