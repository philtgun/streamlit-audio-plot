# streamlit-audio-plot

Streamlit component that allows you to plot audio embeddings as a plotly figure with source audio playback on hover or click.

## Installation instructions

```sh
pip install streamlit-audio-plot
```

## Usage instructions

```python
import streamlit as st

from audio_plot import audio_plot, Events

# minimal example
audio_plot(
    embeddings = [[0.1, 0.2], [0.3, 0.4]],
    urls = [
        "https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3#t=0.0,3.0",
        "https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3#t=60.0,63.0",
    ]
)  

# e.g. metadata is a pd.DataFrame
audio_plot(
    embeddings=metadata[["valence", "arousal"]],
    urls=metadata["urls"],
    labels=[f"{artist}: {title}" for artist, title in zip(metadata["artist"], metadata["title"])],
    event=Events.CLICK,  # or Events.HOVER
    height=800,
    volume=0.4,  # between 0. and 1.
    hidePlayer=true,
)
``` 

See the docstring for full specifications of parameters.

The JS audio playback requires that the user first interacts with the webpage (e.g. by clicking on the page).
Otherwise, React with throw a runtime error that will replace the plot. This should be streamlined in the future to not require page reload. 

## Development instructions

Backend
```sh
python3.11 -m venv venv
source venv/bin/activate
pip install streamlit
streamlit run streamlit run audio_plot/__init__.py
```

Frontend (requires nvm or node.js)
```sh
cd audio_plot/frontend
nvm use
npm install
npm run start
```