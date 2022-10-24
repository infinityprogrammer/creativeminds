from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in creativeminds/__init__.py
from creativeminds import __version__ as version

setup(
	name="creativeminds",
	version=version,
	description="Creative Minds",
	author="RAFI",
	author_email="mrafi@creativeadvtech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
