from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in epictuning/__init__.py
from epictuning import __version__ as version

setup(
	name="epictuning",
	version=version,
	description="car parts",
	author="JOHN RECH CABATANA",
	author_email="cabatana.johnrech.g@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
