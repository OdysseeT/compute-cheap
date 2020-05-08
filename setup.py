import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="computecheap", # Replace with your own username
    version="0.0.1",
    author="Odyssée",
    author_email="otremoulis@gmail.com",
    description="Automativally launch AWS ec2 instance to execute piece of your notebook. Handy for ML and heavy process.",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
