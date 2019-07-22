#Idea of thresholding is to hold pixels between two values 0 and 1
import cv2 as cv
'''type:binary,binaryinv,threstrunc,threshtozero,threstozeroinv,adaptivethreshmeanc,adaptivethreshgaussian
Simple Thesholding:
    cv.THRESH_BINARY
    cv.THRESH_BINARY_INV
    cv.THRESH_TRUNC
    cv.THRESH_TOZERO
    cv.THRESH_TOZERO_INV
Adaptive Thresholding:
    cv.ADAPTIVE_THRESH_MEAN_C 
    cv.ADAPTIVE_THRESH_GAUSSIAN_C 
    '''
class threshold:
    def __init__(self,path,vtype='binary',thres=127,maxval=255,blockSize=11,C=2):
        self.vtype=vtype
        self.path=path
        self.thres=thres
        self.maxval=maxval
        self.blockSize=blockSize
        self.C=C
    def thresholdimage(self):
        img=cv.imread(self.path)
        img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if self.vtype is 'binary':
            return cv.threshold(img,self.thres,self.maxval,cv.THRESH_BINARY)
        elif self.vtype is'binaryinv':
            return cv.threshold(img,self.thres,self.maxval,cv.THRESH_BINARY_INV)
        elif self.vtype is 'threstrunc':
            return cv.threshold(img,self.thres,self.maxval,cv.THRESH_TRUNC)
        elif self.vtype=='threshtozero':
            return cv.threshold(img,self.thres,self.maxval,cv.THRESH_TOZERO)
        elif self.vtype=='threstozeroinv':
            return cv.threshold(img,self.thres,self.maxval,cv.THRESH_TOZERO_INV)
        elif self.vtype=='adaptivethreshmeanc':
            ret,th1 = cv.threshold(img,self.thres,self.maxval,cv.THRESH_BINARY)
            return cv.adaptiveThreshold(img_grey,self.maxval,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,self.blockSize,self.C)
            
        elif self.vtype=='adaptivethreshgaussian':
            ret,th1 = cv.threshold(img,self.thres,self.maxval,cv.THRESH_BINARY)
            return cv.adaptiveThreshold(img_grey,self.maxval,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,self.blockSize,self.C)
        else:
            return None
        