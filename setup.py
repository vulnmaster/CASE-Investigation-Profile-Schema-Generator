from setuptools import setup, find_packages

setup(
    name="case-investigation-schema-generator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["jsonschema>=4.21.1", "rdflib>=7.0.0"],
    extras_require={
        "test": [
            "pytest>=8.3.4",
            "pytest-cov>=6.0.0",
        ],
    },
    python_requires=">=3.7",
    author="Cpry Hall",
    author_email="",
    description="A tool to generate JSON schemas for CASE investigation profiles",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/casework/CASE-Investigation-Profile-Schema-Generator",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
