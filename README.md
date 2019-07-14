# Welcome to Computer Vision Pip Package Docs


## Installation
* pip install computer-vision 

For full documentation visit [https://github.com/nishgaba-ai/computer-vision/blob/master/docs/index.md](https://github.com/nishgaba-ai/computer-vision/blob/master/docs/index.md).

## Modules

* **'loadImage'**  
     **as_bgr()**   # Loads Imge as CV2 BGR format (numpy array as of OpenCV 4)  
     **as_rgb()**   # Loads Image as RGB format using pillow  
* **'loadVideo'**
     **fromCamera**  # Loads from camera from an external source  
     **fromVideo**   # Loads from a video path into the camera  
     **fromPiCamera**   # Loads the video source from Pi Camera  

## Project layout

    src/
        loadImage.py    # Contains modules for Loading Images in differnet formats
        loadVideo.py    # Contains modules for Loading Video using different sources

    mkdocs.yml    # The configuration file.
    docs/
        .. index.md  # The documentation homepage.
