import os
import io
from setuptools import setup, find_packages


# Helpers


def read(*paths):
    """Read a text file."""
    basedir = os.path.dirname(__file__)
    fullpath = os.path.join(basedir, *paths)
    contents = io.open(fullpath, encoding="utf-8").read().strip()
    return contents


# Prepare


PACKAGE = "standards"
NAME = "frictionless-standards"
TESTS_REQUIRE = [
    "black",
    "pylama",
    "pytest",
    "pyright",
    "livemark",
    "pytest-cov",
    "pytest-vcr",
    "pytest-mock",
    "pytest-only",
    "pytest-dotenv",
    "pytest-timeout",
    "pytest-lazy-fixture",
]
EXTRAS_REQUIRE = {
    "dev": TESTS_REQUIRE,
}
INSTALL_REQUIRES = [
    "pyyaml>=5.3",
    "attrs>=22.2.0",
    "pydantic>=2.0a1",
    "jsonschema>=2.5",
]
README = read("README.md")
VERSION = read(PACKAGE, "assets", "VERSION")
PACKAGES = find_packages(exclude=["tests"])
ENTRY_POINTS = {"console_scripts": ["frictionless = frictionless.__main__:program"]}


# Run


setup(
    name=NAME,
    version=VERSION,
    packages=PACKAGES,
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    extras_require=EXTRAS_REQUIRE,
    entry_points=ENTRY_POINTS,
    zip_safe=False,
    long_description=README,
    long_description_content_type="text/markdown",
    description="Lightweight yet comprehensive data standards as Data Package and Table Schema",
    author="Open Knowledge Foundation",
    author_email="info@okfn.org",
    url="https://github.com/frictionlessdata/standards",
    license="MIT",
    keywords=[
        "data validation",
        "frictionless data",
        "open data",
        "json schema",
        "json table schema",
        "data package",
        "tabular data package",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
