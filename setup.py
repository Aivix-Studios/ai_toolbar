from setuptools import setup, find_packages

setup(
    name="ai-toolbar",
    version="1.0.0",
    description="Minimalist desktop toolbar for quick access to AI tools on Linux Mint Xfce",
    author="Aivix Studios",
    author_email="contact@aivix.com",
    packages=find_packages(),
    install_requires=[
        "PyQt5>=5.15.0",
        "PyQtWebEngine>=5.15.0",
        "pynput>=1.7.0",
        "keyring>=23.0.0",
    ],
    entry_points={
        "console_scripts": [
            "ai-toolbar=src.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
)