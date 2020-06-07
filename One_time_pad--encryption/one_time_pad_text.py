import matplotlib.pyplot as plt
import numpy as np

with open ("C:/Users/menta/Desktop/STiOD Lab 1/tekst.txt", "r") as myfile:
    text=myfile.read()

def toASCII(input_text):
    orginal_text = []
    for i in range(len(input_text)):
        char = input_text[i]
        orginal_text.append(ord(char))
    return orginal_text

def fromASCII(input_data):
    text = ""
    for n in input_data:
        text += chr(n)
    return text

def stringcomp(orginal_text,test_text):
    if orginal_text == test_text:
        return True
    else: return False

def key(_length_):
    key = []
    for i in range(_length_):
        key.append(int(np.random.randint(32, 591, 1)))
    return key

def encrypt(input_data,key_):
    cipher = []
    if len(key_)<len(input_data):
        temp = key_
        while len(key_)<len(input_data):
            key_ += temp
    for i in range(len(input_data)):
        cipher.append((input_data[i] + key_[i])%591)
    return cipher

def decrypt(input_data,key_):
    cipher = []
    if len(key_)<len(input_data):
        temp = key_
        while len(key_)<len(input_data):
            key_ += temp
    for i in range(len(input_data)):
        cipher.append((input_data[i]-key_[i])%591)
    return cipher

data = toASCII(text)

key_length = 65536
key_ = key(key_length)

cipher = encrypt(data,key_)
decipher = fromASCII(decrypt(cipher,key_))

#print(decipher)

#print("Encryption is corect: " + str(stringcomp(text,decipher)))


plt.hist(cipher, bins = list(range(32,591)))
plt.savefig('C:/Users/menta/Desktop/STiOD Lab 1/one_time_pad_text_cipher_' + str(key_length) + '_hist.png')
plt.clf()
plt.hist(data, bins = list(range(32,591)))
plt.savefig('C:/Users/menta/Desktop/STiOD Lab 1/one_time_pad_text_orginal_hist.png')