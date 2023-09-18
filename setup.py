from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="streamlit-audio-plot",
    version="0.0.1",
    author="Philip Tovstogan",
    author_email="phil.tovstogan@gmail.com",
    description="Streamlit component that allows you to do plot audio embeddings as a plotly figure with source audio playback on hover or click.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/philtgun/streamlit-audio-plot",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
