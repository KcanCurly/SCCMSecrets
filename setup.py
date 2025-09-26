from setuptools import setup, find_packages

def read_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()

setup(
    name="SCCMSecrets",
    version="1.0.0",
    author="KcanCurly",
    description="SCCMSecrets.py is an SCCM policies exploitation tool.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KcanCurly/SCCMSecrets",
    packages=find_packages(),
    install_requires=read_requirements(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "SCCMSecrets=src.SCCMSecrets:app",
        ],
    },
)