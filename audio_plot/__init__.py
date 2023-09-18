import os
from enum import StrEnum

import numpy as np
import pandas as pd
import streamlit.components.v1 as components

_RELEASE = True


if not _RELEASE:
    _component_func = components.declare_component(
        "audio_plot",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("audio_plot", path=build_dir)

class Events(StrEnum):
    HOVER = "hover"
    CLICK = "click"

def audio_plot(
        embeddings: np.ndarray | list[list] | pd.DataFrame,
        urls: list[str] | pd.Series,
        labels: list[str] | pd.Series = None,
        event: Events = Events.HOVER,
        height: int = 600,
        volume: float = 0.5,
        hidePlayer: bool = False,
        key=None
    ):
    """Create a new instance of "audio_plot".

    Parameters
    ----------
    embeddings: list, np.array or pd.DataFrame with two columns
        2D array that contains the embeddings. Inner dimension should be 2.
    
    urls: list of strings or pd.Series 
        Urls of the audio streams. Can use the format of adding #t=0.0,3.0 
        to the end of the url to specify the start and end time of the segment.

    labels: list of strings or pd.Series 
        Labels of the audio segments that are displayed on hover.

    event: Events.HOVER or Events.CLICK
        Event that triggers the audio playback (HOVER by deafult).

    height: int
        Height of the plot in pixels (600 by default).
    
    volume: float between 0 and 1
        Volume of the audio (0.5 by default).

    hidePlayer: bool
        Hide the audio player (False by default).

    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.
    
    """
    # transform embeddings to list of lists
    if isinstance(embeddings, pd.DataFrame):
        embeddings = embeddings.to_numpy()
    
    if isinstance(embeddings, list):
        embeddings = np.array(embeddings)

    if isinstance(embeddings, np.ndarray):
        embeddings = embeddings.T.tolist()        

    # check shape
    if len(embeddings) != 2:
        raise ValueError("Embeddings must be a 2D array with shape=(2,n), DataFrame with two columns or list of two lists")

    if len(embeddings[0]) != len(embeddings[1]):
        raise ValueError(f"Lists in embeddings must have the same length (0: {embeddings[0]} vs 1: {embeddings[1]})")
    
    # transform urls to list
    if isinstance(urls, pd.Series):
        urls = urls.to_list()

    # transform labels to list
    if isinstance(labels, pd.Series):
        labels = labels.to_list()

    # check lengths
    total = len(embeddings[0])
    if total != len(urls):
        raise ValueError(f"Embeddings and urls must have the same length (embeddings: {len(embeddings[0])} vs urls: {len(urls)})")
    
    return _component_func(
        embeddings=embeddings,
        urls=urls, 
        labels=labels,
        event=event,
        height=height,
        volume=volume,
        hidePlayer=hidePlayer,
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
