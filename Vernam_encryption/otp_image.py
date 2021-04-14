import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2 as cv
from numpy import asarray
from PIL import Image


def fromArray(input_data):
    result = []
    for i in range(len(input_data)):
        result += input_data[i]
    return result

def key_gen(length):      #key generating function
    key = []
    for _ in range(length):     # _ as a throwaway variable
        key.append(int(np.random.randint(0, 255, 1)))
    return key

def encrypt(input_data, key):      #encypting function
    result = []
    if len(key) < (len(input_data) * len(input_data[1])):
        temp = key
        while len(key) < (len(input_data) * len(input_data[1])):
            key += temp
    for i in range(len(input_data)):
        foo = []
        row = input_data[i]
        for j in range(len(row)):
            foo.append((row[j] - key[(len(input_data[1]) * (i-1) ) + j]) %255)
        result.append(foo)
    return np.asarray(result)

def decrypt(input_data, key):      #decypting function
    result = []
    if len(key) < (len(input_data) * len(input_data[1])):
        temp = key
        while len(key) < (len(input_data) * len(input_data[1])):
            key.append(temp)
    for i in range(len(input_data)):
        foo = []
        row = input_data[i]
        for j in range(len(row)):
            foo.append((row[j] + key[(len(input_data[1]) * (i-1) ) + j]) %255)
        result.append(foo)
    return np.asarray(result)

def list_to_string(key_list):      #function translate list into string
    key = ''
    for i in range(len(key_list)):
        key += str(key_list[i]) + ','
    key = key[:-1]
    return key

def string_to_list(key_string):      #function translate string of numbers into list of numbers
    key = []
    key_strlist = key_string.split(',')
    try:
        key = map(int, key_strlist)
        key = list(key)
    except:
        raise ValueError("Key error...")
    return key

def makeHist(img, img_shifted):     #function for drawing histograms
    fig, axs = plt.subplots(2, 1, constrained_layout=True)      #setting subplot 
    fig.suptitle('Comparison of the tonal distribution in the  images.', fontsize=16)       #setting figure title

    color = ('b','g','r')       #tuple of colors indexes
    for i,col in enumerate(color):      #making histogram with each RGB chanel on it 
        hist = cv.calcHist([img_shifted],[i],None,[256],[0,256])        #making one histogram
        axs[0].plot(hist,color = col)       #adding it to subplot
    axs[0].set_title('Histogram of shifted image')      #setting tittle of histogram
    axs[0].set_xlabel('Colors')     # x axis name
    axs[0].set_ylabel('Frequency')      # y axis name


    for i,col in enumerate(color):
        hist = cv.calcHist([img],[i],None,[256],[0,256])
        axs[1].plot(hist,color = col)
    axs[1].set_title('Histogram of original image')
    axs[1].set_xlabel('Colors')
    axs[1].set_ylabel('Frequency')

    plt.show()

def main():     #main function
    print('Do you want encrypt or decrypt image?')
    flag = input('Enter enc or dec: ')     #entering the flag to set performed operation
    if flag.lower() != 'enc' and flag.lower() != 'dec':       #checking if the flag was set correctly
        raise ValueError("You entered wrong value")

    path = input('Enter the file path: ')
    if type(path) != str:       #path must be a string
        raise TypeError("Path must be a string")
    img = Image.open(path).convert('RGB')
    data = np.array(img)
    
    if flag.lower() == 'enc':       #checking if the flag was set to encrypt
        s = int(input('Enter key length: '))     #entering the key length
        key = key_gen(s)
        print(len(key))

        img_mod = encrypt(data, key)       #encrypting image

        print('Do you whant to save key to text file?')
        sav = input('Enter Y or N: ')        #entering the flag for saving the result
        if sav.upper() != 'Y' and sav.upper() != 'N':       #checking if the flag was set correctly
            raise ValueError("You entered wrong value")
        
        if sav.upper() == 'Y':       #checking if the saving flag was set to Y
            with open ('key.txt', "wt", encoding = "utf-8") as myfile:        #saving result
                myfile.write(list_to_string(key))
        elif sav.upper() == 'N':       #checking if the saving flag was set to N
            pass

    elif flag.lower() == 'dec':       #checking if the flag was set to decrypt
        path = input('Enter the path to the text file containing the key: ')        #loading key from txt file
        if type(path) != str:       #path must be a string
            raise TypeError("Path must be a string")
        with open (path, "r", encoding = "utf-8") as myfile:
            key_str = myfile.read()
        key = string_to_list(key_str)       #translating input key string into list

        img_mod = decrypt(data, key)       #decrypting image
    else:       #if the flag was set wrong
        print('Something went wrong ... sorry')

    print('Do you whant to save result?')
    sav = input('Enter Y or N: ')        #entering the flag for saving the result
    if sav.upper() != 'Y' and sav.upper() != 'N':       #checking if the flag was set correctly
        raise ValueError("You entered wrong value")
    
    if sav.upper() == 'Y':       #checking if the saving flag was set to Y
        cv.imwrite('result_img.png', img_mod)      #saving result
    if sav.upper() == 'N':       #checking if the saving flag was set to N
        cv.imshow('Result image',img_mod)       #displaying result
    else:       #if the flag was set wrong
        print('Something went wrong ... sorry')

    print('Do you whant to show histogram')
    his = input('Enter Y or N: ')        #entering the flag for making histogram
    if his.upper() != 'Y' and his.upper() != 'N':       #checking if the flag was set correctly
        raise ValueError("You entered wrong value")
    
    if his.upper() == 'Y':       #checking if the his was set to Y
        makeHist(data,img_mod)      #using makeHist() function
    elif his.upper() == 'N':       #checking if the his was set to N
        pass      #doing nothing
    else:       #if the flag was set wrong
        print('Something went wrong ... sorry')

    
if __name__ == "__main__":
    main()