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

def audio_plot(key=None):
    """Create a new instance of "my_component".

    Parameters
    ----------


    """
    urls = [
            "https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3#t=0.0,3.0",
            "https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3#t=60.0,63.0",
        ]
    return _component_func(x=[0,1], y=[1,-2], urls=urls, height=800, key=key)


if not _RELEASE:
    import streamlit as st

    # Create an instance of our component with a constant `name` arg, and
    # print its output value.
    audio_plot()
