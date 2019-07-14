# Welcome to Computer Vision Pip Package Docs

For full documentation visit [mkdocs.org](https://github.com/nishgaba-ai/computer-vision).

## Modules

* 'loadImage'
     as_bgr()   # Loads Imge as CV2 BGR format (numpy array as of OpenCV 4)\n
     as_rgb()   # Loads Image as RGB format using pillow\n
* 'loadVideo'
     fromCamera  # Loads from camera from an external source\n
     fromVideo   # Loads from a video path into the camera\n
     fromPiCamera   # Loads the video source from Pi Camera\n

## Project layout

    src/
        loadImage.py    # Contains modules for Loading Images in differnet formats
        loadVideo.py    # Contains modules for Loading Video using different sources

    mkdocs.yml    # The configuration file.
    docs/
        .. index.md  # The documentation homepage.

