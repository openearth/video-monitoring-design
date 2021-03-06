# Video Monitoring Design
This repository contains an object-based camera design toolbox, loosely inspired by the work Irv Elshoff [RIP] did in Deltares, between 2010 and 2013. Primitive code was written in MATLAB. Adapted, re-built and optimized in 2021.

The tool returns camera footprint, camera longshore and cross-shore pixel resolutions and a table with data per camera. 
New cameras and lenses can be added in `availableCamerasAndLenses.py` together with their image size in pixel and field of view. All physical settings such as camera locations, background image, plot names and limits and can be given as input in `PROTOTYPE.py`.

### Install 
Create an pip [environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) and run

`python -m pip install -r requirements.txt`

### Run
`python main.py`

### Results
<img src="https://github.com/openearth/video-monitoring-design/raw/main/src/footprint.png" width="500" height="600">
<img src="https://github.com/openearth/video-monitoring-design/raw/main/src/resolution/longshore-res.png" width="1000" height="250">
<img src="https://github.com/openearth/video-monitoring-design/raw/main/src/resolution/crossshore-res.png" width="1000" height="250">
<img src="https://github.com/openearth/video-monitoring-design/raw/main/src/table.png" width="1000">
