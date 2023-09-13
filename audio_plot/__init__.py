import os

import numpy as np
import pandas as pd
import streamlit.components.v1 as components

_RELEASE = False


if not _RELEASE:
    _component_func = components.declare_component(
        "audio_plot",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend-react/build")
    _component_func = components.declare_component("audio_plot", path=build_dir)

def audio_plot(
        embeddings: np.ndarray | list[list] | pd.DataFrame,
        urls: list[str] | pd.Series,
        labels: list[str] | pd.Series = None,
        height: int = 600,
        volume: float = 0.4,
        key=None
    ):
    """Create a new instance of "audio_plot".

    Parameters
    ----------


    """
    # transform embeddings to list of lists
    if type(embeddings) is pd.DataFrame:
        embeddings = embeddings.to_numpy()
    
    if type(embeddings) is list:
        embeddings = np.array(embeddings)

    if type(embeddings) is np.ndarray:
        embeddings = embeddings.T.tolist()        

    if len(embeddings) != 2:
        raise ValueError("Embeddings must be a 2D array with shape=(2,n), DataFrame with two columns or list of two lists")

    if len(embeddings[0]) != len(embeddings[1]):
        raise ValueError(f"Lists in embeddings must have the same length (0: {embeddings[0]} vs 1: {embeddings[1]})")
    
    # transform urls to list
    if type(urls) is pd.Series:
        urls = urls.to_list()

    # transform labels to list
    if type(labels) is pd.Series:
        labels = labels.to_list()

    # check lengths
    total = len(embeddings[0])
    if total != len(urls):
        raise ValueError(f"Embeddings and urls must have the same length (embeddings: {len(embeddings[0])} vs urls: {len(urls)})")
    
    return _component_func(
        embeddings=embeddings,
        urls=urls, 
        labels=labels,
        height=height,
        volume=volume,
        key=key
    )


if not _RELEASE:
    import streamlit as st

    # Create an instance of our component with a constant `name` arg, and
    # print its output value.
    _urls = [
        "https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3#t=0.0,3.0",
        "https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3#t=60.0,63.0",
    ]
    
    audio_plot(
        embeddings=[[1,1], [2,2]], 
        urls=_urls,
        labels=["Track 1", "Track 2"],
    )
