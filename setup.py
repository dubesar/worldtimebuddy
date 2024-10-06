from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='worldtimebuddy',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'pytz',
    ],
    entry_points='''
        [console_scripts]
        worldtimebuddy=worldtimebuddy.cli:cli
    ''',
    description='A command-line tool to display current time for different timezones',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Sarvesh Dubey',
    author_email='dubeysarvesh5525@gmail.com',
    url='https://github.com/dubesar/worldtimebuddy',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)