import pandas as pd
import numpy as np
from ipywidgets import Output, GridspecLayout
from IPython import display
from IPython.display import HTML
from ucimlrepo import fetch_ucirepo 



def DisplayCVDVideos():
    videos = HTML("""
        <details>
        <summary>Click to show/hide videos</summary>
        <div style="text-align: center;">
        <div style="display: inline-block; padding: 100px;">
                <iframe width="150%" height="315" src="https://www.youtube.com/embed/g131j2lb3xw" frameborder="0" allowfullscreen></iframe>
            </div>
            <div style="display: inline-block; padding: 100px;">
                <iframe width="150%" height="315" src="https://www.youtube.com/embed/6LbKWBjOa1A" frameborder="0" allowfullscreen></iframe>
            </div>
        </div>
        </details>
        """)
    return videos

def Fetch_CVD_Data():
    heart_disease = fetch_ucirepo(id=45) 
    X = heart_disease.data.features 
    y = heart_disease.data.targets 
    X['num'] = y
    return X