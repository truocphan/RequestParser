# python setup.py bdist_wheel sdist
# twine upload --skip-existing dist/*
import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="RequestParser",
	version="22.6.12",
	author="Truoc Phan",
	license="MIT",
	author_email="truocphan112017@gmail.com",
	description="",
	long_description=long_description,
	long_description_content_type="text/markdown",
	install_requires=[],
	url="https://github.com/truocphan/RequestParser",
	classifiers=[
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 2",
		"Programming Language :: Python :: Implementation :: Jython"
	],
	keywords=["Request Parser"],
	packages=["RequestParser"],
)
