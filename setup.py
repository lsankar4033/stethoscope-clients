from setuptools import setup, find_packages

with open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="stethoscope-clients",
    description="Eth2 clients packaged for networking tests",
    version="0.1.1",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="lsankar4033",
    author_email="lsankar4033@gmail.com",
    url="https://github.com/lsankar4033/stethoscope-clients",
    python_requires=">=3.8, <4",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    tests_require=[
        "pytest>=5.4.1,<6",
        "pytest-trio==0.6.0"
    ],
    install_requires=[
        "pyrum>=0.2.1,<0.3.0",
        "trio==0.15.0",
        "tenacity==6.2.0"
    ],
    include_package_data=True,
    keywords=["networking", "eth2", "stethoscope"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
    ],
)
