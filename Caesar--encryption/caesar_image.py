import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def encrypt(input_data,s):      #encypting function
    result = []
    for i in range(len(input_data)):        #iterating through rows of pixels
        foo = []
        row = input_data[i]
        for j in range(len(row)):       #iterating through pixels in each row
            foo.append((row[j] + s)%255)        #changing pixel value by adding shift, modulo keeps the value between 0 and 255
        result.append(foo)
    return np.array(result)

def decrypt(input_data,s):      #decypting function
    result = []
    for i in range(len(input_data)):        #iterating through rows of pixels
        foo = []
        row = input_data[i]
        for j in range(len(row)):       #iterating through pixels in each row
            foo.append((row[j] - s)%255)        #changing pixel value by subtracting shift, modulo keeps the value between 0 and 255
        result.append(foo)
    return np.array(result)

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

    s = int(input('Enter value of shift: '))     #entering the shift valueenc
    
    if flag.lower() == 'enc':       #checking if the flag was set to encrypt
        img_mod = encrypt(data,s)       #encrypting image
    elif flag.lower() == 'dec':       #checking if the flag was set to decrypt
        img_mod = decrypt(data,s)       #decrypting image
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