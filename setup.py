from setuptools import setup

with open("docs/index.md", "r") as fh:
    long_description = fh.read()

setup(
    name ='computer-vision',
    author_email='nishchal@unrealai.xyz',
    author='Nishchal Gaba',
    url='https://github.com/nishgaba-ai/computer-vision',
    version='0.0.6',
    description='Machine Learning utilities to make your Project Development Life easier',
    py_modules=["loadImage", "loadVideo", "utils", "networkRequests"],
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)


















