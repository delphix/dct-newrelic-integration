#
# Copyright (c) 2022 by Delphix. All rights reserved.
#

from setuptools import find_packages
from setuptools import setup
from src.main import VERSION

# Get the long description from the README file
long_description = "This is an executable for the Delphix Integration for New Relic"

setup(
    version=VERSION,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Customers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Monitoring",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    install_requires=[
        "newrelic-telemetry-sdk==0.4.3",
        "requests==2.31.0",
        "tenacity==8.1.0",
    ],
    # Format is mypkg.mymodule:the_function'
    entry_points="""
        [console_scripts]
        nr=src.main:run
    """,
    author="Delphix Engineering",
    keywords="new-relic, delphix, dct",  # noqa
    license="Apache 2",
    description="Delphix Integration for New Relic",
    dependency_links=[],
    name="delphix-nr",
    long_description_content_type="text/markdown",
    long_description=long_description,
    include_package_data=True,
    project_urls={},  # Optional
)
