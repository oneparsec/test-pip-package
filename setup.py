import setuptools


setuptools.setup(
    name="testpackage",
    version="0.1",
    author="OneParsec",
    author_email="dontsendmailhere@example.com",
    description="Test Pip Package",
    long_description="# TEST",
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "testpackage = testpackage.main:main",
        ],
    },
    install_requires=[
        "clint",
        "pycryptodomex",
        "requests"
    ],
    python_requires='>=3.6',
)