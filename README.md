# Video Monitoring Design
This repository contains an object-based camera design toolbox, loosely inspired by the work Irv Elshoff [RIP] did in Deltares, between 2010 and 2013. Primitive code was written in MATLAB. Adapted, re-built and optimized in 2021.

The tool returns camera footprint, camera longshore and cross-shore pixel resolutions and a table with data per camera. 
New cameras and lenses can be added in `availableCamerasAndLenses.py` together with their image size in pixel and field of view. All physical settings such as camera locations, background image, plot names and limits and can be given as input in `PROTOTYPE.py`.

## Install 
Create an pip [environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) and run
`python -m pip install -r requirements.txt`

## Run
`python main.py`


![footprint](https://raw.githubusercontent.com/openearth/video-monitoring-design/src/footprint.png)
![longshore](https://raw.githubusercontent.com/openearth/video-monitoring-design/src/resolution/longshore-res.png)
![crossshore](https://raw.githubusercontent.com/openearth/video-monitoring-design/src/resolution/crossshore-res.png)
![table](https://raw.githubusercontent.com/openearth/video-monitoring-design/src/table.png)
