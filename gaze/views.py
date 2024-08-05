from flask import render_template
import os

from . import gaze

@gaze.route('/')
def index():
    return render_template(
        'gaze/index.html', 
        ROBOFLOW_API_KEY=os.environ.get("ROBOFLOW_API_KEY"),
        ANALYTICS_ID=os.environ.get("ANALYTICS_ID")
    )