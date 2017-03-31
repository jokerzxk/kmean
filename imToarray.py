#coding=utf-8
from PIL import Image
from numpy import *
import scipy
import matplotlib.pyplot as plt

def ImageToMatrix(filename):
    im = Image.open(filename)

    im.show()  
    width,height = im.size
    im = im.convert("L") 
    data = im.getdata()
    
    print data
    data = matrix(data,dtype='float')/1024.0
    new_data = reshape(data,(width,height))
    print '123',type(data)
    return new_data
#     new_im = Image.fromarray(new_data)

    new_im.show()
def MatrixToImage(data):
    data = data*255
    new_im = Image.fromarray(data.astype(uint8))

    print type(data),type(data.astype(uint8))
    return new_im



filename = '30k.jpg'
data = ImageToMatrix(filename)
print type(data)
new_im = MatrixToImage(data)
#plt.imshow(data, cmap=plt.cm.gray, interpolation='nearest')
new_im.show()
new_im.save('lena_1.bmp')