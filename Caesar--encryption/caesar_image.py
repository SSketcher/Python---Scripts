import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy import asarray
from PIL import Image

img = Image.open('C:/Users/menta/Desktop/STiOD Lab 1/Przykładowe obrazy-20200306/a.png')
data = asarray(img)


def encrypt(input_data,s): 
    result = []
    for i in range(len(input_data)):
        foo = []
        row = input_data[i]
        for j in range(len(row)):
            foo.append((row[j] - s)%255)
        result.append(foo)
    return np.asarray(result)

def decrypt(input_data,s): 
    result = []
    for i in range(len(input_data)):
        foo = []
        row = input_data[i]
        for j in range(len(row)):
            foo.append(row[j] + s)
        result.append(foo)
    return np.asarray(result)

def fromArray(input_data):
    result = []
    for i in range(len(input_data)):
        result += input_data[i]
    return result


s=120


cipher = encrypt(data,s)
decipher = decrypt(cipher,s)

img_encrypt = Image.fromarray(cipher)
img_encrypt.show()
#img_encrypt.save("C:/Users/menta/Desktop/STiOD Lab 1/img_encrypt_" + str(s) + "_hist.jpg")

img_encrypt = Image.fromarray(decipher)
#img_encrypt.show()


plt.hist(fromArray(cipher.tolist()), bins = list(range(0,255)))
plt.savefig('C:/Users/menta/Desktop/STiOD Lab 1/cesar_image_cipher_' + str(s) + '_hist.png')
plt.clf()
plt.hist(fromArray(data.tolist()), bins = list(range(0,255)))
plt.savefig('C:/Users/menta/Desktop/STiOD Lab 1/cesar_image_orginal_hist.png')