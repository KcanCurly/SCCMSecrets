from setuptools import setup, find_packages

setup(
    name="SCCMSecrets",
    version="1.0.0",
    author="KcanCurly",
    description="lateral movement script that leverages the CcmExec service to remotely hijack user sessions.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KcanCurly/SCCMSecrets",
    packages=find_packages(),
    install_requires=[
        "requests",
        "typer[all]",
        "bs4",
        "cryptography",
        "requests_ntlm",
        "requests_toolbelt",
        "pyasn1_modules"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "SCCMSecrets=src.SCCMSecrets:app",
        ],
    },
)