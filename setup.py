from setuptools import find_packages, setup

with open("README.md") as file:
    long_description = file.read()

setup(
    name="tkup",
    version="1.1.0",
    description="Hierarchical Tkinter wrapper",
    long_description=long_description,
    url="https://github.com/mtkennerly/tkup",
    author="Matthew T. Kennerly (mtkennerly)",
    author_email="mtkennerly@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: User Interfaces"
    ],
    keywords="gui tkinter wrapper",
    packages=find_packages()
)
