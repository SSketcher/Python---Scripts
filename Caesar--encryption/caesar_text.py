import matplotlib.pyplot as plt

with open ("C:/Users/menta/Desktop/STiOD Lab 1/tekst.txt", "r") as myfile:
    text=myfile.read()


def fromASCII(input_data):
    text = ""
    for n in input_data:
        text += chr(n)
    return text

def toASCII(input_text):
    orginal_text = []
    for i in range(len(input_text)):
        char = input_text[i]
        orginal_text.append(ord(char))
    return orginal_text

def stringcomp(orginal_text,test_text):
    if orginal_text == test_text:
        return True
    else: return False

def encrypt(input_data,key_):
    cipher = []
    for i in range(len(input_data)):
        cipher.append((input_data[i] + s)%591)
    return cipher

def decrypt(input_data,key_):
    cipher = []
    for i in range(len(input_data)):
        cipher.append((input_data[i] - s)%591)
    return cipher



s = 20



cipher = encrypt(toASCII(text),s)
decipher = fromASCII(decrypt(cipher,s))

print("Encryption is corect: " + str(stringcomp(text,decipher)))


plt.hist(cipher, bins = list(range(32,591)))
plt.savefig('C:/Users/menta/Desktop/STiOD Lab 1/cesar_text_cipher_' + str(s) + '_hist.png')
plt.clf()
plt.hist(toASCII(text), bins = list(range(32,591)))
plt.savefig('C:/Users/menta/Desktop/STiOD Lab 1/cesar_text_orginal_hist.png')