from setuptools import setup, find_packages

project_name = "tidepool_data_science_project"
version = "0.0.3"
author = "Your Name"
author_email = "YourName@tidepool.org"
package_name = "tidepool_data_science_project"  # this is the thing you actually import

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=project_name,
    version=version,
    author=author,
    author_email=author_email,
    description="Python repository to facilitate using the Tidepool API (forked). ",
    packages=find_packages(),  # add subpackages too
    package_dir={package_name: package_name},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/miriamkw/data-science-tidepool-api-python",
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
