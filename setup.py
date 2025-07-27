#!/usr/bin/env python3
"""Setup script for ai_toolbar package."""

from setuptools import setup, find_packages

# Read the README file for long description, with error handling
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = ""

setup(
    name="ai_toolbar",
    version="0.1.0",
    author="Aivix Studios",
    description="Minimalist desktop toolbar for quick access to AI tools on Linux Mint Xfce",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aivix-Studios/ai_toolbar",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Desktop Environment",
    ],
    python_requires=">=3.6",
    install_requires=[
        # Add dependencies here as needed
    ],
    entry_points={
        "console_scripts": [
            "ai-toolbar=ai_toolbar.main:main",
        ],
    },
)