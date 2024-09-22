from setuptools import find_packages, setup

setup(
    name="mathCustom",
    version="0.1.0",
    description="A module for complex numbers and vectors",
    author="AVER3LL",
    author_email="Sainque@proton.me",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],  # External dependencies, if any (e.g., numpy)
)
