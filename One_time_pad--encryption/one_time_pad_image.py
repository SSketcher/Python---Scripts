import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy import asarray
from PIL import Image

img = Image.open('C:/Users/menta/Desktop/STiOD Lab 1/Przykładowe obrazy-20200306/b.png')
data = asarray(img)


def key(_length_):
    key = []
    for i in range(_length_):
        key.append(int(np.random.randint(0, 255, 1)))
    return key

def encrypt(input_data,key_):
    result = []
    if len(key_)<len(input_data[1]):
        temp = key_
        while len(key_)<(len(input_data)*len(input_data[1])):
            key_ += temp
    print(len(key_))
    for i in range(len(input_data)):
        foo = []
        row = input_data[i]
        for j in range(len(row)):
            foo.append((row[j] - key_[(len(input_data[1]) *(i-1) ) + j])%255)
        result.append(foo)
    return np.asarray(result)

def decrypt(input_data,key_):
    key_count = 1
    result = []
    if len(key_)<(len(input_data)*len(input_data[1])):
        temp = key_
        while len(key_)<(len(input_data)*len(input_data[1])):
            key_.append(temp)
    for i in range(len(input_data)):
        foo = []
        row = input_data[i]
        for j in range(len(row)):
            foo.append(row[j] + key_[key_count])
            key_count += 1
        result.append(foo)
    return np.asarray(result)

def fromArray(input_data):
    result = []
    for i in range(len(input_data)):
        result += input_data[i]
    return result



key_length = 20
key_ = key(key_length)

print(key_)

cipher = encrypt(data,key_)
#decipher = decrypt(encrypt_data,key_)

img_encrypt = Image.fromarray(cipher)
img_encrypt.show()

#img_decrypt = Image.fromarray(decrypt_data)
#img_decrypt.show()


plt.hist(fromArray(cipher.tolist()), bins = list(range(0,255)))
plt.savefig('C:/Users/menta/Desktop/STiOD Lab 1/one_time_pad_image_b_' + str(key_length) + '_hist.png')
plt.clf()
plt.hist(fromArray(data.tolist()), bins = list(range(0,255)))
plt.savefig('C:/Users/menta/Desktop/STiOD Lab 1/cesar_image_orginal_hist.png')