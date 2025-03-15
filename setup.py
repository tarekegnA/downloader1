from setuptools import setup, find_packages

setup(
    name="advanced_downloader",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A fast and efficient downloader software using Aria2 and Kivy.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tarekegnA/downloader",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "kivy==2.2.1",
        "aria2p==0.11.0",
        "requests==2.31.0",
        "asyncio==3.4.3",
        "jsonschema==4.19.2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "downloader=main:main",
        ],
    },
)
