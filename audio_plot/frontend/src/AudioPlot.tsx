import {
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode, createRef } from "react"
import Plot from 'react-plotly.js'

interface State { }

/**
 * This is a React-based component template. The `render()` function is called
 * automatically when your component should be re-rendered.
 */
class AudioPlot extends StreamlitComponentBase<State> {
  private audioPlayerRef = createRef<HTMLAudioElement>()

  // constructor(props: any) {
  //   super(props);
  //   this.audioPlayerRef = React.createRef();
  // }

  public state = {}

  public render = (): ReactNode => {
    const { args } = this.props

    // Streamlit sends us a theme object via props that we can use to ensure
    // that our component has visuals that match the active theme in a
    // streamlit app.
    const { theme } = this.props
    const style: React.CSSProperties = {
      height: args.height,
    }

    // Maintain compatibility with older versions of Streamlit that don't send
    // a theme object.
    if (theme) {

    }

    return (
      <div style={style}>
        <Plot
          data={[
            {
              x: args.embeddings[0],
              y: args.embeddings[1],
              type: 'scatter',
              mode: 'markers',
              text: args.labels,
              hoverinfo: 'text',
            },
          ]}
          layout={{
            margin: {
              b: 0,
              t: 0,
              l: 0,
              r: 0,
            },
            xaxis: {
              showgrid: false,
              zeroline: false,
              visible: false,
            },
            yaxis: {
              showgrid: false,
              zeroline: false,
              visible: false,
            },
            paper_bgcolor: 'rgba(0,0,0,0.05)',
            plot_bgcolor: 'rgba(0,0,0,0.05)',
          }}
          config={{
            scrollZoom: true,
          }}
          onHover={args.event === "hover" ? this._playAudioOnEvent : undefined}
          onClick={args.event === "click" ? this._playAudioOnEvent : undefined}
        />
        <audio
          style={{ margin: 'auto', display: 'block' }}
          ref={this.audioPlayerRef}
          controls={!args.hidePlayer}
        />
      </div>
    )
  }

  private playAudio = (url: string) => {
    console.log(this.audioPlayerRef)
    const audioElement: any = this.audioPlayerRef.current
    if (audioElement) {
      audioElement.src = url
      audioElement.volume = this.props.args.volume
      audioElement.play()
    }
  }

  private _playAudioOnEvent = (event: any) => {
    const url = this.props.args.urls[event.points[0].pointIndex]
    this.playAudio(url)
  }

}

// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
export default withStreamlitConnection(AudioPlot)
