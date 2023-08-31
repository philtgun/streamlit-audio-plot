import os

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
    name: str
        The name of the thing we're saying hello to. The component will display
        the text "Hello, {name}!"
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    """
    return _component_func(data={}, key=key)



if not _RELEASE:
    import streamlit as st

    # Create an instance of our component with a constant `name` arg, and
    # print its output value.
    audio_plot()
