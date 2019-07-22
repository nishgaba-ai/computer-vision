import cv2 as cv
import numpy as np
class ImageDenoising:
  def __init__(self,path,variation='MD',dst=None,templateWindowSize=7,searchWindowSize=21,h=3):
    '''variation can have two values:
      -'MD'-cv.fastNlMeansDenoising() - works with a single grayscale images
      -'MDC'-cv.fastNlMeansDenoisingColored() - works with a color image.
    '''
    self.variation=variation
    self.path=path
    self.dst=dst
    self.templateWindowSize=templateWindowSize
    self.searchWindowSize=searchWindowSize
    self.h=h
    self.hForColorComponents=self.h
    
  def denoising(self): 
    img=cv.imread(self.path)
    ''' Common-arguments-
            src-Input 8-bit 1-channel, 2-channel, 3-channel or 4-channel image.
            dst-Output image with the same size and type as src .
            hForColorComponents : same as h, but for color images only. (normally same as h) 
            templateWindowSize-Size in pixels of the template patch that is used to compute weights. Should be odd. Recommended value 7 pixels
            searchWindowSize-Size in pixels of the window that is used to compute weighted average for given pixel. 
                            Should be odd. Affect performance linearly: greater searchWindowsSize - greater denoising time. Recommended value 21 pixels
            h-Parameter regulating filter strength. Big h value perfectly removes noise but also removes image details, smaller h value preserves details 
                            but also preserves some noise'''
    if self.variation is 'MD': #works with a single grayscale images
      return cv.fastNlMeansDenoising(img,self.dst,self.templateWindowSize,self.searchWindowSize,self.h) 
    elif self.variation is 'MDC':
      return cv.fastNlMeansDenoisingColored(img,self.dst,self.templateWindowSize,self.hForColorComponents,self.searchWindowSize,self.h)
    
    
        