import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy import asarray
from PIL import Image
from scipy.io import loadmat

img = Image.open('C:/Users/menta/Desktop/STiOD Lab 2/dane/test.png')
data_img = asarray(img)

data_keys = loadmat('C:/Users/menta/Desktop/STiOD Lab 2/dane/hasla.mat')

def mattolist(input_data):
    result = []
    foo = input_data['hasla'].tolist()
    for item in foo:
        result.append(item[0].tolist()[0])
    return result



def dictionaryAttack(photo,dictionary):
    def decrypt(input_data,key_):
        result = []
        if len(key_)<len(input_data[1]):
            temp = key_
            while len(key_)<(len(input_data)*len(input_data[1])):
                key_ += temp
        for i in range(len(input_data)):
            foo = []
            row = input_data[i]
            for j in range(len(row)):
                foo.append((row[j] + key_[(len(input_data[1]) *(i-1) ) + j])%255)
            result.append(foo)
        return np.asarray(result)
    
    result = []
    for i in range(1,3):
        result.append(decrypt(photo,dictionary[i-1]))
    return result


#keys = mattolist(data_keys)

keys = [[132, 236, 41, 182, 24, 32, 174, 14, 158, 125, 251, 242, 119, 251, 97, 181, 11, 117, 189, 129],[1,2,3,4,5]]

print(len(keys))

decipher = dictionaryAttack(data_img,keys)

imgs = plt.figure()
counter = 1
for i in range(1,2):
    for j in range(1,3):
        img = Image.fromarray(decipher[counter-1])
        imgs.add_subplot(2,5,counter)
        plt.title('Image ' + str(counter) )
        plt.imshow(img)
        counter +=1
        
        
plt.show() 