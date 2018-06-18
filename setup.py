from setuptools import setup

setup(
    name='hello',
    py_modules=['hello'],
    scripts=['bin/hello'],
    test_suite='hello.test',
)
