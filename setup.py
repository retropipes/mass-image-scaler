import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mass-image-scaler-wrldwzrd89",
    version="0.0.1",
    author="Eric Ahnell",
    author_email="eric.ahnell@puttysoftware.com",
    description="Batch image scaling with the ScaleYx algorithm family",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wrldwzrd89/mass-image-scaler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)