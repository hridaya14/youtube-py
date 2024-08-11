import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="youtube_wrapper_py",
    version="0.0.2",
    author="Hridaya Sharma",
    author_email="hridaya.02819011622@ipu.ac.in",
    description="This is a package that wraps around the YouTube API, providing an easier user interface and experience",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hridaya14/youtube-py",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=[
        "python-dotenv>=0.21.0",
        "youtube-transcript-api>=0.4.1",
        "google-api-python-client>=2.64.0"
    ],
)
