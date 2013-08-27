from setuptools import setup

setup(
	name='termcolors',
	version='0.1.0',
	description='Show off your beautiful terminal palette',
	long_description=open('README.rst').read(),
	url='http://github.com/scizzorz/termcolors',
	license='MIT',
	author='John Weachock',
	author_email='jweachock@gmail.com',
	py_modules=['termcolors'],
	include_package_data=True,
	scripts=['bin/termcolors'],
)
