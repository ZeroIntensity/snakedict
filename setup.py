from setuptools import setup

with open("./README.md") as f:
    long_desc: str = f.read()

if __name__ == "__main__":
    setup(
        name="snakedict",
        version="1.0.0",
        author="ZeroIntensity",
        author_email="<zintensitydev@gmail.com>",
        description="Keep your dict keys PEP 8 compliant.",
        long_description_content_type="text/markdown",
        long_description=long_desc,
        py_modules=["snakedict"],
        install_requires=["typing_extensions"],
        keywords=["python", "pep 8", "dicts"],
        classifiers=[
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
        ],
        license="MIT",
        urls={"Repo": "https://github.com/ZeroIntensity/snakedict"},
    )
