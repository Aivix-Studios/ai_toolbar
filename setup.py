#!/usr/bin/env python3
"""
Setup script for AI Toolbar

Installs the AI Toolbar desktop application package.
"""

from setuptools import setup, find_packages
from pathlib import Path
import sys

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# Read requirements
requirements = []
with open('requirements.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('-'):
            # Handle conditional requirements
            if ';' in line:
                req, condition = line.split(';', 1)
                requirements.append(line)
            else:
                requirements.append(line)

setup(
    name="ai-toolbar",
    version="1.0.0",
    author="Aivix-Studios",
    author_email="contact@aivix.com",
    description="Minimalist desktop toolbar for quick access to AI tools on Linux Mint Xfce",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aivix-Studios/ai_toolbar",
    project_urls={
        "Bug Tracker": "https://github.com/Aivix-Studios/ai_toolbar/issues",
        "Documentation": "https://github.com/Aivix-Studios/ai_toolbar#readme",
        "Source Code": "https://github.com/Aivix-Studios/ai_toolbar",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "": ["resources/config.json", "resources/icons/*", "resources/styles/*"],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Desktop Environment",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-qt>=4.2.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
        ],
        "packaging": [
            "pyinstaller>=5.0.0",
            "build>=0.8.0",
            "twine>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "ai-toolbar=main:main",
        ],
        "gui_scripts": [
            "ai-toolbar-gui=main:main",
        ],
    },
    keywords="ai, toolbar, desktop, linux, pyqt5, artificial-intelligence, productivity",
    platforms=["Linux"],
    zip_safe=False,
)