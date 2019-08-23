import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="odufrn_api_py",
    version="0.0.1",
    author="Open Data UFRN",
    author_email="alvarofepipa@gmail.com",
    description="Open Data UFRN API Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/odufrn/odufrn-api-py",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
